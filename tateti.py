
import os
from colorama import Fore, Style, init

# Inicializa colorama para que los colores funcionen en la consola.
# El parámetro 'autoreset=True' asegura que el color vuelva al estado por defecto
# después de cada 'print', para que no afecte a futuros textos.
init(autoreset=True)

# Definimos los colores para X y O. Usamos 'Fore' para el color del texto
# y 'Style.BRIGHT' para que el color sea más intenso y visible.
COLOR_X = Fore.RED + Style.BRIGHT + 'X'
COLOR_O = Fore.BLUE + Style.BRIGHT + 'O'

def crear_tablero():
    """
    Crea un tablero de 3x3.
    Se representa como una lista de 9 elementos, cada uno inicializado con un espacio
    para indicar que la celda está vacía.
    """
    return [' '] * 9

def mostrar_tablero(tablero):
    """
    Muestra el tablero en la consola de una manera visualmente atractiva.
    
    Args:
        tablero (list): La lista que representa el estado actual del tablero.
    """
    # Limpia la pantalla para dar la ilusión de un tablero que se actualiza.
    # 'cls' es para Windows y 'clear' es para Linux/macOS.
    os.system('cls' if os.name == 'nt' else 'clear') 
    
    print("\n--- Ta-Te-Ti ---")
    print("----------------")
    
    # Bucle para imprimir cada fila del tablero.
    for i in range(3):
        # Muestra la fila actual, accediendo a los elementos de la lista.
        # Por ejemplo, para la primera fila, accede a tablero[0], tablero[1], tablero[2].
        print(f" {tablero[i*3]} | {tablero[i*3+1]} | {tablero[i*3+2]} ")
        
        # Dibuja la línea horizontal entre las filas.
        if i < 2:
            print("---+---+---")
    print("----------------\n")

def verificar_ganador(tablero, jugador):
    """
    Verifica si un jugador ha ganado el juego.
    
    Args:
        tablero (list): El estado actual del tablero.
        jugador (str): La marca del jugador a verificar ('X' o 'O').
        
    Returns:
        bool: True si el jugador ha ganado, False en caso contrario.
    """
    # Lista de todas las posibles combinaciones ganadoras (filas, columnas y diagonales).
    condiciones_ganadoras = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Filas
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columnas
        (0, 4, 8), (2, 4, 6)             # Diagonales
    ]
    
    # Recorre cada combinación ganadora para ver si coincide con la marca del jugador.
    for condicion in condiciones_ganadoras:
        if tablero[condicion[0]] == tablero[condicion[1]] == tablero[condicion[2]] == jugador:
            return True
    return False

def es_empate(tablero):
    """
    Verifica si el juego ha terminado en un empate.
    Un empate ocurre cuando no hay más espacios vacíos en el tablero.
    
    Args:
        tablero (list): El estado actual del tablero.
        
    Returns:
        bool: True si es un empate, False si aún hay espacios.
    """
    return ' ' not in tablero

def jugar():
    """
    Función principal que contiene el bucle del juego.
    Gestiona el flujo del juego, los turnos y el final del mismo.
    """
    tablero = crear_tablero()
    # El juego siempre comienza con el jugador 'X'.
    jugador_actual = COLOR_X
    
    while True:
        mostrar_tablero(tablero)
        
        # Muestra el jugador actual sin los códigos de color para una mejor lectura en el mensaje.
        jugador_sin_color = 'X' if jugador_actual == COLOR_X else 'O'
        print(f"Es el turno de {jugador_sin_color}.")
        
        try:
            # Solicita al usuario que ingrese una posición del 1 al 9.
            # Se resta 1 para que la entrada del usuario (1-9) corresponda al índice de la lista (0-8).
            posicion = int(input("Elige una posición (1-9): ")) - 1
            
            # Verifica si la posición elegida es válida (entre 0 y 8) y si la celda está vacía.
            if 0 <= posicion <= 8 and tablero[posicion] == ' ':
                # Si la posición es válida, se coloca la marca del jugador actual en el tablero.
                tablero[posicion] = jugador_actual
                
                # Después de cada movimiento, se verifica si hay un ganador.
                if verificar_ganador(tablero, jugador_actual):
                    mostrar_tablero(tablero)
                    print(f"¡Felicidades! ¡El jugador {jugador_sin_color} ha ganado!")
                    break  # Rompe el bucle y termina el juego.
                
                # Si no hay ganador, se verifica si el juego es un empate.
                if es_empate(tablero):
                    mostrar_tablero(tablero)
                    print("¡El juego ha terminado en empate!")
                    break  # Rompe el bucle y termina el juego.
                
                # Si no hay ganador ni empate, se cambia al siguiente jugador.
                jugador_actual = COLOR_O if jugador_actual == COLOR_X else COLOR_X
            else:
                # Mensaje de error si la posición no es válida o está ocupada.
                print("Posición inválida o ya ocupada. Inténtalo de nuevo.")
        
        except ValueError:
            # Captura un error si el usuario no ingresa un número.
            print("Entrada no válida. Por favor, ingresa un número del 1 al 9.")

# Esta es la línea que inicia el juego cuando se ejecuta el script.
if __name__ == "__main__":
    jugar()