import sys
import pygame
from config import *
from aleatorias import *
from random import randint, randrange
from pygame import display, time, draw, event
from colisones import *
from pygame.locals import *

def terminar():
    pygame.quit()
    exit()

def mostrar_texto(superficie, texto, fuente, coordenadas, color_fuente, color_fondo=BLACK):
    sup_texto = fuente.render(texto, True, color_fuente, color_fondo)
    rect_texto = sup_texto.get_rect()
    rect_texto.center = coordenadas
    superficie.blit(sup_texto, rect_texto)

def wait_user():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminar()
    
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminar()
                return

def crear_bloque(imagen = None, left=0, top=0, ancho=50, alto=50, color=(255, 255, 255), dir=3, borde=0, radio=-1, speed_x=5, speed_y=5):
    rec = pygame.Rect(left, top, ancho, alto)
    if imagen:
        imagen = pygame.transform.scale(imagen, (ancho, alto))
    return {"rect": rec, "color": color, "dir": dir, "borde": borde, "radio": radio, "speed_x": speed_x, "speed_y": speed_y, "imagen": imagen}

def handler_new_coin():
    coins.append(crear_bloque(None, randint(0, width - size_coin), randint(0, height - size_coin), size_coin, size_coin, CUSTOM, radio = size_coin // 2))
    
def load_coins_list(coins, cantidad, imagen = None):
    for i in range(cantidad):
        size_coin = randint(size_min_coin, size_max_coin)
        coins.append(crear_bloque(imagen, randint(0, width - size_coin), randint(0, height - size_coin), size_coin, size_coin, YELLOW, radio = size_coin // 2))
        
def dibujar_asteroides(superficie, coins):
    for coin in coins:
        if coin["imagen"]:
            superficie.blit(coin["imagen"], coin["rect"])
        else:
            draw.rect(superficie, coin["color"], coin["rect"], coin["borde"], coin["radio"])

# Inicializar todos los modulos
pygame.init()

# Tamaño de pantalla (superficie)
screen = pygame.display.set_mode(size_screen)
# Duración de cada iteración
clock = pygame.time.Clock()
# Nombre del juego
pygame.display.set_caption("Primer Jueguito")
# Cambiar color
screen.fill(CUSTOM)
# Draw
draw = pygame.draw

# Cargo sonidos
coin_sound = pygame.mixer.Sound("./src/assets/coin.mp3")
game_over_sound = pygame.mixer.Sound("./src/assets/game-over.mp3")
appear_sound = pygame.mixer.Sound("./src/assets/appear.mp3")
victory_sound = pygame.mixer.Sound("./src/assets/victory.mp3")

# Volumen sonidos
pygame.mixer.music.load("./src/assets/musicafondo.mp3")
# pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)
coin_sound.set_volume(0.1)
appear_sound.set_volume(0.1)
playing_music = True

# Cargo imagenes
image_player = pygame.image.load("./src/assets/ovni.png")
image_asteroid = pygame.image.load("./src/assets/asteroide.png")
image_asteroid_2 = pygame.image.load("./src/assets/asteroide-2.png")
image_asteroid_3 = pygame.image.load("./src/assets/asteroide-3.png")
background = pygame.transform.scale(pygame.image.load("./src/assets/background-b1.jpg"), size_screen)

# Evento personalizado

EVENT_NEW_COIN = pygame.USEREVENT + 1
pygame.time.set_timer(EVENT_NEW_COIN, 2000)

cont_grande = 0
count_coins = 10
max_contador = 0

# Direccion / Movimiento
move_up = False
move_right = False
move_down = False
move_left = False
contador = 0

# Fuente
fuente = pygame.font.SysFont(None, 48)

# texto = fuente.render(f"Coins: {contador}", True, CUSTOM)
# rect_texto = texto.get_rect()
# rect_texto.midtop = (width // 2, 30)   

# Creo el rectangulo
block = crear_bloque(image_player, randint(0, width - BLOCK_WIDTH), randint(0, height - BLOCK_WIDTH), BLOCK_WIDTH, BLOCK_HEIGHT, RED, radio= 25)

# Crear lista de coins
# coins = []
# load_coins_list(coins, count_coins, image_asteroid)

# Variable de control
is_running = True

screen.fill(BLACK)
mostrar_texto(screen, "Asteroides", fuente, (width // 2, 40), CUSTOM)
mostrar_texto(screen, "Presione una tecla para comenzar...", fuente, center_screen, CUSTOM)
pygame.display.flip()
wait_user()

pygame.mouse.set_visible(False)

while True:
    
    contador = 0
    texto = fuente.render(f"Coins: {contador}", True, CUSTOM)
    rect_texto = texto.get_rect()
    rect_texto.midtop = (width // 2, 30)   
    tiempo_juego = FPS * 10
    is_running = True
    pygame.mixer.music.play(-1) 
    
    coins = []
    load_coins_list(coins, count_coins, image_asteroid) 
      
    while is_running:
        clock.tick(FPS)
        print(len(coins))
        # ---> Detectar los eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                is_running = False   
            if event.type == EVENT_NEW_COIN:
                handler_new_coin()
                
            if event.type == KEYDOWN:
                if event.key == K_RIGHT or event.key == K_d:
                    move_right = True
                    move_left = False
                if event.key == K_LEFT or event.key == K_a:
                    move_left = True
                    move_right = False
                if event.key == K_UP or event.key == K_w:
                    move_up = True
                    move_down = False
                if event.key == K_DOWN or event.key == K_s:
                    move_down = True
                    move_up = False
                    
                if event.key == K_m:
                    if playing_music:
                        pygame.mixer.music.pause()
                    else:                        
                        pygame.mixer.music.unpause()
                    playing_music = not playing_music
                    
                # Pausa juego
                
                if event.key == K_p:
                    if playing_music:
                        pygame.mixer.music.pause()
                    mostrar_texto(screen, "Pausa", fuente, center_screen, CUSTOM, BLACK)
                    pygame.display.flip()
                    wait_user()
                    if playing_music:
                        pygame.mixer.music.unpause()

                
            if event.type == KEYUP:
                if event.key == K_RIGHT or event.key == K_d:
                    move_right = False
                if event.key == K_LEFT or event.key == K_a:
                    move_left = False
                if event.key == K_UP or event.key == K_w:
                    move_up = False
                if event.key == K_DOWN or event.key == K_s:
                    move_down = False
                
                # Para cerrar el juego con ESC
                if event.key == K_ESCAPE:
                    is_running = False
                            
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    new_coin = crear_bloque(None, event.pos[0], event.pos[1], size_coin, size_coin, WHITE, radio = size_coin // 2)
                    new_coin["rect"].left -= size_coin // 2
                    new_coin["rect"].top -= size_coin // 2
                    coins.append(new_coin)
                if event.button == 3:
                    block["rect"].center = (center_screen)
            
            if event.type == MOUSEMOTION:
                block["rect"].center = (event.pos[0], event.pos[1])
                
        # ---> Actualizar los elementos
                
        # Movimiento del bloque de acuerdo a su direccion
        if move_right and block["rect"].right <= (width - SPEED):
            # Derecha
            block["rect"].left += SPEED
        if move_left and block["rect"].left >= (0 + SPEED):
            # Izquierda
            block["rect"].left -= SPEED
        if move_up and block["rect"].top >= SPEED:
            # Arriba
            block["rect"].top -= SPEED
        if move_down and block["rect"].bottom < height - SPEED:
            # Abajo
            block["rect"].top += SPEED
            
        pygame.mouse.set_pos(block["rect"].centerx, block["rect"].centery)
            
        for coin in coins[ : ]:
            if detectar_colision_circ(coin["rect"], block["rect"]):
                coins.remove(coin)
                contador += 1
                texto = fuente.render(f"Coins: {contador}", True, CUSTOM, BLACK)
                rect_texto = texto.get_rect()
                rect_texto.midtop = (width // 2, 30)      
                cont_grande = 10
                if playing_music:
                    coin_sound.play()
                
                if len(coins) == 0:
                    load_coins_list(coins, count_coins, image_asteroid_2)
                    if playing_music:
                        coin_sound.play()
                
        if cont_grande > 0:
            cont_grande -= 1
            block["rect"].width = BLOCK_WIDTH * 1.3
            block["rect"].height = BLOCK_HEIGHT * 1.3
            block["color"] = color_aleatorio()
        else:
            block["rect"].width = BLOCK_WIDTH 
            block["rect"].height = BLOCK_HEIGHT
            block["color"] = RED
            
        # ---> Dibujar pantalla
        # screen.fill(BLACK)
        screen.blit(background, origin)
        
        dibujar_asteroides(screen, coins)
                
        screen.blit(block["imagen"], block["rect"])
        
        screen.blit(texto, rect_texto)
        
        # ---> Actualizar pantalla, puede ser flip o update()
        pygame.display.flip()
        
        if tiempo_juego == 0:
            is_running = False
    
    if contador > max_contador:
        max_contador = contador
    
    screen.fill(BLACK)
    pygame.mixer.music.stop()
    game_over_sound.play()
    mostrar_texto(screen, f"Max score: {max_contador}", fuente, (width // 2, 30), CUSTOM)
    mostrar_texto(screen, "GAME OVER", fuente, center_screen, CUSTOM)
    mostrar_texto(screen, "Presione una tecla para continuar...", fuente, (width // 2, height - 30), CUSTOM)
    pygame.display.flip()
    wait_user()
            
terminar()