# registro-mtga-meta

Lista del meta de **Standard** que usa *Registro MTGA* para poner nombre al mazo del rival (compara las cartas que
ha jugado con los arquetipos más jugados y elige el que más coincide).

- `meta_standard.json` — la lista. Se actualiza cada 3 días.
- Dirección para el programa (Ajustes › Mazos del meta):
  `https://raw.githubusercontent.com/EusebioG96/registro-mtga-meta/main/meta_standard.json`

## Formato

```json
{
  "formato": "standard",
  "fecha": "AAAA-MM-DD",
  "fuente": "…",
  "arquetipos": [
    {"nombre": "Dimir Midrange", "colores": "UB", "meta": 9.4,
     "cartas": {"Kaito, Bane of Nightmares": [4.0, 100, 0, null], "Duress": [0, null, 3.1, 80]}}
  ]
}
```

Cada carta: `[copias medias en el principal, % de listas que la llevan en el principal, copias medias en el
banquillo, % en el banquillo]` (`null` si la fuente no da el porcentaje). Las tierras básicas no hacen falta.
`meta` es la cuota de meta en %. `colores` en orden WUBRG.

## Cómo se actualiza

Ver [ACTUALIZAR.md](ACTUALIZAR.md). Antes de publicar: `python3 herramientas/validar.py`.

Datos de metajuego: [MTGGoldfish](https://www.mtggoldfish.com/metagame/standard/full) (desglose medio de cartas
por arquetipo). Registro MTGA es contenido de fans no oficial; no está aprobado ni respaldado por Wizards of the Coast.
