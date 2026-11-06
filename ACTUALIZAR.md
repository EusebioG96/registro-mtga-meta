# Procedimiento de actualización

Cada 3 días se actualiza Standard y, además, el formato con la fecha más antigua de entre Pioneer, Modern, Legacy,
Vintage y Pauper. `<formato>` es el nombre en minúsculas: standard, pioneer, modern, legacy, vintage o pauper.

1. Abrir `https://www.mtggoldfish.com/metagame/<formato>/full` y apuntar los arquetipos con su cuota (%) y la ruta
   de su página (`/archetype/<formato>-…`). Quedarse con los que tengan **0,4 % o más** (unos 30).
2. Para cada arquetipo, abrir su página y leer el *card breakdown*: para cada carta, copias medias y % de listas,
   en principal y en banquillo. Omitir las tierras básicas.
3. Colores del arquetipo (WUBRG) a partir de su nombre y de sus tierras/cartas (p. ej. Dimir = UB, Jund = BRG,
   «Lifegain» con Godless Shrine = WB, «4c» = los cuatro colores que usen sus tierras). Un mazo incoloro lleva `colores` vacío.
4. Escribir `meta_<formato>.json` con el formato del README y la fecha de hoy. Mantener los mismos nombres de
   arquetipo que en la versión anterior cuando sea el mismo mazo (así el historial del usuario no cambia de nombre).
5. `python3 herramientas/validar.py` → debe decir OK.
6. Si la lista apenas ha cambiado (mismos arquetipos y cartas), basta con actualizar la fecha. Publicar con un
   commit «Meta de <Formato> AAAA-MM-DD» en `main`.
7. Si MTGGoldfish no responde o su página cambia de forma que no se puede leer bien, NO publicar una lista
   incompleta: dejar la anterior y explicar el problema en el resumen.
