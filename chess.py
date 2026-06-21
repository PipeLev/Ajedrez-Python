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
    
    if movimiento in pieza or movimiento in peones:
        # Guardamos el nombre de la pieza que se va a mover
        pieza_a_mover = movimiento 
        
        movimiento_2 = input("¿A qué columna (A-H) y a qué fila (1-8) va? ").strip().upper()
        patron = re.search(r'([A-H])([1-8])', movimiento_2)
        
        match patron:
            case None:
                print("Coordenada inválida. Formato correcto: Letra A-H y Número 1-8.")
                
            case objeto_match:
                columna = objeto_match.group(1)
                fila = objeto_match.group(2)
                
                # --- NUEVO MATCH INTERNO ESTRUCTURAL ---
                # Evaluamos la tupla (columna, fila)
                match (columna, fila):
                    # El 'if' aquí actúa como un filtro guardián para asegurar los rangos
                    case (c, f) if c in "ABCDEFGH" and f in "12345678":
                        casilla_objetivo = f"{c}{f}"
                        
                        print(f"\n[SISTEMA]: Casilla {casilla_objetivo} detectada exitosamente.")
                        
                        # Cambiamos la casilla en cuestión por la pieza usada
                        tablero[casilla_objetivo] = pieza_a_mover
                        
                        print(f"¡Movimiento realizado! La casilla {casilla_objetivo} ahora contiene: {pieza_a_mover}")
                        check.append((c, f))



                        
                        
                    case _:
                        # Por si la expresión regular dejó pasar algo extraño
                        print("Error crítico: Posición fuera del rango del tablero.")
    else:
        print("Esa pieza no existe en tu tablero. Intenta de nuevo.")