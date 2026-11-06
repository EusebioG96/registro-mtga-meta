#!/usr/bin/env python3
"""Comprueba que un meta_<formato>.json es válido antes de publicarlo (lo mismo que comprueba ManaLab al descargarlo,
y algo más). Sin argumentos valida los seis formatos. Uso: python3 herramientas/validar.py [meta_modern.json ...]"""
import json, re, sys
import glob

def validar(ruta):
    d = json.load(open(ruta, encoding="utf-8"))
    errores = []
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", str(d.get("fecha") or "")): errores.append("fecha AAAA-MM-DD")
    arqs = d.get("arquetipos")
    if not isinstance(arqs, list) or len(arqs) < 15: errores.append("al menos 15 arquetipos")
    for a in arqs or []:
        n = a.get("nombre")
        if not n: errores.append("arquetipo sin nombre"); continue
        if not re.fullmatch(r"[WUBRG]{0,5}", a.get("colores") or ""): errores.append(f"{n}: colores en WUBRG (vacío si es incoloro)")
        if not isinstance(a.get("meta"), (int, float)) or a["meta"] <= 0: errores.append(f"{n}: meta > 0")
        c = a.get("cartas") or {}
        if len(c) < 8: errores.append(f"{n}: pocas cartas ({len(c)})")
        for carta, v in c.items():
            if not (isinstance(v, list) and len(v) == 4): errores.append(f"{n}/{carta}: [copias, %, copias banquillo, % banquillo]"); break
    total = sum(a.get("meta", 0) for a in arqs or [])
    print(f"{ruta}: {len(arqs or [])} arquetipos · {total:.1f} % del meta · fecha {d.get('fecha')}")
    if errores:
        print("ERRORES:\n- " + "\n- ".join(errores)); return False
    print("OK")
    return True

rutas = sys.argv[1:] or sorted(glob.glob("meta_*.json"))
sys.exit(0 if all([validar(r) for r in rutas]) else 1)
