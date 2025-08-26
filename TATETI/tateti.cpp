#include "raylib.h"    // Incluye la biblioteca principal de Raylib
#include <iostream>    // Para el uso de entrada/salida estándar (opcional, no se usa en este código)
#include <vector>      // Para usar la estructura de datos dinámica std::vector

// Definiciones de constantes del juego
#define SCREEN_WIDTH 600   // Ancho de la ventana en píxeles
#define SCREEN_HEIGHT 600  // Altura de la ventana en píxeles
#define CELL_SIZE 200      // Tamaño de cada celda del tablero

// Definiciones de colores personalizados
Color COLOR_X = { 255, 0, 0, 255 };         // Rojo (Rojo, Verde, Azul, Alfa)
Color COLOR_O = { 0, 0, 139, 255 };         // Azul marino
Color COLOR_FONDO = { 255, 240, 245, 255 }; // Blanco rosado para el fondo
Color COLOR_LINEAS = { 255, 0, 255, 255 };   // Fucsia vibrante
Color COLOR_MENSAJE = { 255, 0, 0, 255 };    // Rojo para los mensajes finales

// Enumeración para representar el estado del juego de forma más legible
enum GameState {
    PLAYING,         // El juego está en curso
    PLAYER_1_WINS,   // El Jugador 1 ('X') ha ganado
    PLAYER_2_WINS,   // El Jugador 2 ('O') ha ganado
    DRAW             // El juego es un empate
};

// Variables del juego
std::vector<char> board(9, ' '); // Un vector de 9 caracteres para el tablero. 
                                   // Se inicializa con espacios en blanco.
int currentPlayer = 1;             // 1 para Jugador X, 2 para Jugador O
GameState gameState = PLAYING;     // El juego comienza en estado 'jugando'

// Prototipos de funciones
void DrawBoard();    // Dibuja el tablero, las 'X's y las 'O's
void HandleInput();  // Captura y procesa la entrada del mouse
void CheckWin();     // Revisa si la partida ha terminado

// Función principal del programa
int main(void) {
    // Inicialización de la ventana de Raylib
    InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, "Ta Te Ti en C++");
    SetTargetFPS(60); // Limita los FPS para un juego fluido

    // Bucle principal del juego. Se ejecuta hasta que la ventana se cierre.
    while (!WindowShouldClose()) {
        HandleInput();  // Maneja la entrada del usuario (clic del mouse)
        CheckWin();     // Revisa si alguien ha ganado o si hay un empate

        // Sección de dibujo: todo lo que se dibuja en pantalla
        BeginDrawing();                             // Comienza a dibujar
        ClearBackground(COLOR_FONDO);               // Pinta el fondo con el color personalizado
        
        DrawBoard();                                // Llama a la función para dibujar el tablero y las fichas

        if (gameState != PLAYING) {                 // Si el juego ha terminado...
            std::string message;
            if (gameState == PLAYER_1_WINS) {
                message = "¡Jugador 1 (X) gana!";
            } else if (gameState == PLAYER_2_WINS) {
                message = "¡Jugador 2 (O) gana!";
            } else if (gameState == DRAW) {
                message = "¡Empate!";
            }
            
            // Dibuja el mensaje final en el centro de la pantalla
            DrawText(message.c_str(), SCREEN_WIDTH / 2 - MeasureText(message.c_str(), 40) / 2, SCREEN_HEIGHT / 2 - 20, 40, COLOR_MENSAJE);
        }

        EndDrawing(); // Finaliza el dibujo y lo muestra en pantalla
    }

    CloseWindow();    // Cierra la ventana y limpia todos los recursos
    return 0;         // Retorna 0 para indicar que el programa se ejecutó sin errores
}

// Función que dibuja el tablero y las marcas de los jugadores
void DrawBoard() {
    // Dibuja las líneas de la cuadrícula
    for (int i = 1; i < 3; i++) {
        DrawLine(i * CELL_SIZE, 0, i * CELL_SIZE, SCREEN_HEIGHT, COLOR_LINEAS);
        DrawLine(0, i * CELL_SIZE, SCREEN_WIDTH, i * CELL_SIZE, COLOR_LINEAS);
    }

    // Recorre el vector para dibujar las fichas en cada celda
    for (int i = 0; i < 9; i++) {
        // Calcula las coordenadas x e y de la celda actual
        int x = (i % 3) * CELL_SIZE;
        int y = (i / 3) * CELL_SIZE;
        
        if (board[i] == 'X') {
            // Dibuja una 'X' usando el color rojo personalizado
            DrawLine(x + 20, y + 20, x + CELL_SIZE - 20, y + CELL_SIZE - 20, COLOR_X);
            DrawLine(x + 20, y + CELL_SIZE - 20, x + CELL_SIZE - 20, y + 20, COLOR_X);
        } else if (board[i] == 'O') {
            // Dibuja una 'O' con el color azul marino personalizado
            DrawCircleLines(x + CELL_SIZE / 2, y + CELL_SIZE / 2, CELL_SIZE / 2 - 20, COLOR_O);
        }
    }
}

// Función que maneja la entrada del mouse del usuario
void HandleInput() {
    // Solo se puede hacer una jugada si el juego está en curso
    if (IsMouseButtonPressed(MOUSE_LEFT_BUTTON) && gameState == PLAYING) {
        Vector2 mousePos = GetMousePosition();    // Obtiene la posición del cursor
        int col = (int)mousePos.x / CELL_SIZE;    // Convierte la posición X en un índice de columna
        int row = (int)mousePos.y / CELL_SIZE;    // Convierte la posición Y en un índice de fila
        int index = row * 3 + col;                // Combina la fila y columna en un único índice (0-8)

        // Verifica si la celda es válida y está vacía
        if (index >= 0 && index < 9 && board[index] == ' ') {
            if (currentPlayer == 1) {
                board[index] = 'X';   // Coloca una 'X'
                currentPlayer = 2;    // Cambia al turno del Jugador 2
            } else {
                board[index] = 'O';   // Coloca una 'O'
                currentPlayer = 1;    // Cambia al turno del Jugador 1
            }
        }
    }
}

// Función que verifica si la partida ha terminado
void CheckWin() {
    // Definir las 8 combinaciones ganadoras (índices del vector)
    const int winningCombos[8][3] = {
        {0, 1, 2}, {3, 4, 5}, {6, 7, 8}, // Filas
        {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, // Columnas
        {0, 4, 8}, {2, 4, 6}             // Diagonales
    };

    // Revisa todas las combinaciones para encontrar un ganador
    for (int i = 0; i < 8; i++) {
        int a = winningCombos[i][0];
        int b = winningCombos[i][1];
        int c = winningCombos[i][2];
        
        // Si las tres celdas en la combinación no están vacías y son iguales...
        if (board[a] != ' ' && board[a] == board[b] && board[b] == board[c]) {
            // Asigna el estado de victoria al jugador correspondiente
            gameState = (board[a] == 'X') ? PLAYER_1_WINS : PLAYER_2_WINS;
            return; // Termina la función ya que se encontró un ganador
        }
    }

    // Si no hay ganador, revisa si hay un empate
    bool isDraw = true;
    for (char cell : board) {
        if (cell == ' ') { // Si encuentra una celda vacía...
            isDraw = false;  // ...entonces no es un empate
            break;           // Y sale del bucle
        }
    }
    if (isDraw) {
        gameState = DRAW; // Si el bucle terminó y todas las celdas estaban llenas, es un empate
    }
}