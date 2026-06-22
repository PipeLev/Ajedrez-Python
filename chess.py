import re
from collections import Counter
import table

tablero = {f"{c}{f}": " " for c in "ABCDEFGH" for f in "12345678"}

# Traemos tus datos originales del archivo table.py
tab = table.tab
tipos = table.tipos

# Diccionario para traducir el número que escribe el usuario al nombre de la fila
# Nota que usamos tipos[1] para el 1 ("ONE"), tipos[2] para el 2 ("TWO"), etc.
CONVERTIR_FILA = {
    "1": tipos[1],  # "ONE"
    "2": tipos[2],  # "TWO"
    "3": tipos[3],  # "THRE"
    "4": tipos[4],  # "FOUR"
    "5": tipos[5],  # "FIVE"
    "6": tipos[6],  # "SIX"
    "7": tipos[7],  # "SEVEN"
    "8": tipos[8]   # "EIGHT"
}

# Diccionario para traducir la letra de la columna a su índice correspondiente (0 al 7)
CONVERTIR_COLUMNA = {
    "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7
}

pieza = table.tab["ONE"]
peones = table.tab["TWO"]

check = [] 

while True:
    movimiento = input("¿Qué pieza desea mover? ").strip()
    
    # 1. Buscamos la pieza en TODO el diccionario para encontrar su fila de origen
    fila_origen = ""
    columna_origen_idx = -1
    
    for f_nombre in tipos[1:]:  # Ignoramos la fila de "letras"
        if movimiento in tab[f_nombre]:
            fila_origen = f_nombre
            columna_origen_idx = tab[f_nombre].index(movimiento)
            break

    # Si fila_origen se quedó vacía, significa que la pieza no existe en el tablero
    if fila_origen != "":
        pieza_a_mover = movimiento
        
        # --- NUEVA VERIFICACIÓN DE COLOR ---
        # Si estaba en ONE o TWO es Blanca, si estaba en SEVEN o EIGHT es Negra
        if fila_origen in ["ONE", "TWO"]:
            color = "Blanca"
        elif fila_origen in ["SEVEN", "EIGHT"]:
            color = "Negra"
        else:
            color = "Desconocido (Casilla vacía previamente)"
        
        print(f"[INFO]: Has seleccionado una pieza {color} ({pieza_a_mover})")
        # ------------------------------------

        movimiento_2 = input("¿A qué columna (A-H) y a qué fila (1-8) va? ").strip().upper()
        patron = re.search(r'([A-H])([1-8])', movimiento_2)
        
        match patron:
            case None:
                print("Coordenada inválida. Formato correcto: Letra A-H y Número 1-8.")
                
            case objeto_match:
                columna = objeto_match.group(1)
                fila = objeto_match.group(2)
                
                match (columna, fila):
                    case (c, f) if c in CONVERTIR_COLUMNA and f in CONVERTIR_FILA:
                        fila_destino = CONVERTIR_FILA[f]
                        columna_destino_idx = CONVERTIR_COLUMNA[c]
                        
                        # Borramos la pieza de su posición anterior
                        tab[fila_origen][columna_origen_idx] = "  "
                        
                        # Colocamos la pieza en su nuevo destino
                        tab[fila_destino][columna_destino_idx] = pieza_a_mover
                        
                        print(f"\n[SISTEMA]: Movimiento ejecutado por las {color}s.")
                        print(f"La pieza {pieza_a_mover} se movió a la casilla {c}{f}.\n")
                        
                        # Mostramos el tablero actualizado
                        table.tablero(tab, tipos)
                        break
                        
                    case _:
                        print("Error crítico: Posición fuera del rango del tablero.")
    else:
        print("Esa pieza no existe o ya fue capturada. Intenta de nuevo.")