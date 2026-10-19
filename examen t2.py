
laberinto = [
    ['F', 1, 0, 0, 0, 0, 0, 0, 0],
    [ 4,  1, 0, 0, 4, 3, 4, 1, 0],
    [ 3,  0, 0, 0, 3, 0, 0, 1, 0],
    [ 4,  4, 3, 1, 4, 0, 0, 4, 0],
    [ 0,  0, 0, 0, 0, 0, 0, 3, 0],
    [ 0,  1, 3, 4, 1, 3, 4, 4, 0],
    [ 0,  4, 0, 0, 0, 0, 0, 0, 0],
    [ 0,  3, 4, 3, 1, 4, 1, 1, 1],
    ['I', 0, 0, 0, 0, 0, 0, 0, 1]
]

FILAS = 9
COLUMNAS = 9


solucion = [[" " for _ in range(COLUMNAS)] for _ in range(FILAS)]


visitado = [[False for _ in range(COLUMNAS)] for _ in range(FILAS)]

def imprimir_laberinto(matriz, titulo):
    """Función para imprimir de forma ordenada el laberinto"""
    print(f"\n--- {titulo} ---")
    for fila in matriz:
        print(" ".join(f"{str(celda):>2}" for celda in fila))

def obtener_valor(celda):
    """Retorna el valor numérico de la celda. 'I' y 'F' equivalen a 1"""
    if celda == 'I' or celda == 'F':
        return 1
    return int(celda)

def es_valido(x, y):
    """Valida que los índices estén dentro del rango y la celda sea transitable"""
    if 0 <= x < FILAS and 0 <= y < COLUMNAS:
        # No es pared (0) y no ha sido visitado en el camino actual
        if laberinto[x][y] != 0 and not visitado[x][y]:
            return True
    return False

def resolver_laberinto_util(x, y, puntos_actuales):
    """Función recursiva de Backtracking para buscar el camino correcto"""
    
    
    valor_celda = obtener_valor(laberinto[x][y])
    puntos_totales = puntos_actuales + valor_celda
    
    
    visitado[x][y] = True
    solucion[x][y] = str(laberinto[x][y])
    
    
    if x == 0 and y == 0:
        
        if puntos_totales >= 23:
            print(f"\n[ÉXITO] ¡Destino alcanzado con {puntos_totales} puntos!")
            return True
        else:
            
            visitado[x][y] = False
            solucion[x][y] = " "
            return False

    
    movimientos = [
        (-1,  0),  # Arriba
        ( 0,  1),  # Derecha
        ( 1,  0),  # Abajo
        ( 0, -1)   # Izquierda
    ]
    
    for dx, dy in movimientos:
        nuevo_x = x + dx
        nuevo_y = y + dy
        
        if es_valido(nuevo_x, nuevo_y):
            if resolver_laberinto_util(nuevo_x, nuevo_y, puntos_totales):
                return True

    
    visitado[x][y] = False
    solucion[x][y] = " "
    return False

def resolver():
    """Función principal que coordina la ejecución"""
    imprimir_laberinto(laberinto, "LABERINTO ORIGINAL")
    
   
    x_inicio, y_inicio = 8, 0
    
    if resolver_laberinto_util(x_inicio, y_inicio, 0):
        imprimir_laberinto(solucion, "MATRIZ DE LA SOLUCIÓN (CAMINO EXPOSITOR)")
    else:
        print("\n[FALLO] No se encontró ningún camino viable que sume 23 o más puntos.")
        imprimir_laberinto(solucion, "MATRIZ DE LA SOLUCIÓN VACÍA")

if __name__ == "__main__":
    resolver()
