#!/usr/bin/env python3
"""Comprueba que un meta_<formato>.json es válido antes de publicarlo (lo mismo que comprueba ManaLab al
descargarlo, y algo más). Uso: python3 herramientas/validar.py [meta_standard.json]
Colores: WUBRG en ese orden; un arquetipo incoloro (p. ej. Eldrazi o Tron incoloros) lleva colores vacío ""."""
import json, re, sys
ruta = sys.argv[1] if len(sys.argv) > 1 else "meta_standard.json"
d = json.load(open(ruta, encoding="utf-8"))
errores = []
if not re.match(r"^\d{4}-\d{2}-\d{2}$", str(d.get("fecha") or "")): errores.append("fecha AAAA-MM-DD")
esperado = re.match(r"meta_(\w+)\.json$", ruta.split("/")[-1])
if esperado and d.get("formato") != esperado.group(1): errores.append(f"formato debe ser «{esperado.group(1)}» (como el nombre del archivo)")
arqs = d.get("arquetipos")
if not isinstance(arqs, list) or len(arqs) < 15: errores.append("al menos 15 arquetipos")
for a in arqs or []:
    n = a.get("nombre")
    if not n: errores.append("arquetipo sin nombre"); continue
    if not re.fullmatch(r"W?U?B?R?G?", a.get("colores") or ""): errores.append(f"{n}: colores en orden WUBRG (o vacío si es incoloro)")
    if not isinstance(a.get("meta"), (int, float)) or a["meta"] <= 0: errores.append(f"{n}: meta > 0")
    c = a.get("cartas") or {}
    if len(c) < 8: errores.append(f"{n}: pocas cartas ({len(c)})")
    for carta, v in c.items():
        if not (isinstance(v, list) and len(v) == 4): errores.append(f"{n}/{carta}: [copias, %, copias banquillo, % banquillo]"); break
total = sum(a.get("meta", 0) for a in arqs or [])
print(f"{len(arqs or [])} arquetipos · {total:.1f} % del meta · fecha {d.get('fecha')}")
if errores:
    print("ERRORES:\n- " + "\n- ".join(errores)); sys.exit(1)
print("OK")
