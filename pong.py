
import pygame
import random

# Inicialización de Pygame
pygame.init()

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Tamaño de la pantalla
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600

# Creación de la pantalla
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Pong")

# Coordenadas de la pelota y de las paletas
pelota_x = ANCHO_PANTALLA // 2
pelota_y = ALTO_PANTALLA // 2
velocidad_pelota_x = 0.4
velocidad_pelota_y = 0.4
jugador_x = 50
jugador_y = ALTO_PANTALLA // 2 - 50
computadora_x = ANCHO_PANTALLA - 50
computadora_y = ALTO_PANTALLA // 2 - 50
jugador_puntos = 0

# Tamaño de las paletas
ANCHO_PALETAS = 20
ALTO_PALETAS = 100

# Velocidad de las paletas
VELOCIDAD_JUGADOR = 0.8
VELOCIDAD_COMPUTADORA = 0.5
# Definir la velocidad de movimiento de la paleta del jugador
jugador_y_cambio = 0

# Bucle principal del juego
while True:
    # Eventos
        # Detectar eventos de teclado
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Mover la paleta del jugador con las teclas de flecha
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                jugador_y_cambio = -1
            elif evento.key == pygame.K_DOWN:
                jugador_y_cambio = 1

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
                jugador_y_cambio = 0

    # Mover la paleta del jugador
    jugador_y += jugador_y_cambio

    # Comprobar límites de la paleta del jugador
    if jugador_y < 0:
        jugador_y = 0
    elif jugador_y > ALTO_PANTALLA - ALTO_PALETAS:
        jugador_y = ALTO_PANTALLA - ALTO_PALETAS

    
    # Movimiento de la pelota
    pelota_x += velocidad_pelota_x
    pelota_y += velocidad_pelota_y

    # Movimiento de la paleta de la computadora
    if pelota_y < computadora_y + ALTO_PALETAS // 2:
        computadora_y -= VELOCIDAD_COMPUTADORA
    elif pelota_y > computadora_y + ALTO_PALETAS // 2:
        computadora_y += VELOCIDAD_COMPUTADORA

    # Comprobar colisiones con el borde superior e inferior
    if pelota_y > ALTO_PANTALLA - 20 or pelota_y < 0:
        velocidad_pelota_y = -velocidad_pelota_y
    
    # Comprobar colisiones con las paletas
    if pelota_x < jugador_x + ANCHO_PALETAS and pelota_x > jugador_x and pelota_y < jugador_y + ALTO_PALETAS and pelota_y > jugador_y:
        velocidad_pelota_x = -velocidad_pelota_x
        jugador_puntos += 20
    elif pelota_x > computadora_x - ANCHO_PALETAS and pelota_x < computadora_x and pelota_y < computadora_y + ALTO_PALETAS and pelota_y > computadora_y:
        velocidad_pelota_x = -velocidad_pelota_x

        # Comprobar si alguien ganó
    if jugador_puntos == 1000:
        fuente = pygame.font.Font(None, 48)
        mensaje = fuente.render("¡Felicidades, ganaste!", True, BLANCO)
        pantalla.blit(mensaje, (ANCHO_PANTALLA // 2 - mensaje.get_width() // 2, ALTO_PANTALLA // 2 - mensaje.get_height() // 2))
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.quit()
        quit()

    # Dibujar todo en la pantalla
    pantalla.fill(NEGRO)
    pygame.draw.rect(pantalla, BLANCO, [pelota_x, pelota_y, 20, 20])
    pygame.draw.rect(pantalla, BLANCO, [jugador_x, jugador_y, ANCHO_PALETAS, ALTO_PALETAS])
    pygame.draw.rect(pantalla, BLANCO, [computadora_x, computadora_y, ANCHO_PALETAS, ALTO_PALETAS])
    texto_puntos = "Puntos: " + str(jugador_puntos)
    fuente_puntos = pygame.font.Font(None, 36)
    mensaje_puntos = fuente_puntos.render(texto_puntos, True, BLANCO)
    pantalla.blit(mensaje_puntos, (ANCHO_PANTALLA - mensaje_puntos.get_width() - 10, 10))

    # Actualización de la pantalla
    pygame.display.update()

if __name__ == '__main__':
    webview.create_window("Juego Pong", "juego_pong.html", width=600, height=400)
