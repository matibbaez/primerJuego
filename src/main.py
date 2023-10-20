import sys
import pygame
from config import *
from aleatorias import *
from random import randint, randrange
from pygame import display, time, draw, event
from colisones import *
from pygame.locals import *

def crear_bloque(imagen, left=0, top=0, ancho=50, alto=50, color=(255, 255, 255), dir=3, borde=0, radio=-1, speed_x=5, speed_y=5):
    rec = pygame.Rect(left, top, ancho, alto)
    return {"rect": rec, "color": color, "dir": dir, "borde": borde, "radio": radio, "speed_x": speed_x, "speed_y": speed_y, "img": imagen}

def handler_new_coin():
    coins.append(crear_bloque(randint(0, width - size_coin), randint(0, height - size_coin), size_coin, size_coin, CUSTOM, radio = size_coin // 2))
    
def load_coins_list(coins, cantidad):
    for i in range(cantidad):
        size_coin = randint(size_min_coin, size_max_coin)
        coins.append(crear_bloque(randint(0, width - size_coin), randint(0, height - size_coin), size_coin, size_coin, YELLOW, radio = size_coin // 2))

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
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)
coin_sound.set_volume(0.1)
appear_sound.set_volume(0.1)
playing_music = True

# Cargo imagenes
image_player = pygame.image.load("./src/assets/ovni.png")

# Evento personalizado

EVENT_NEW_COIN = pygame.USEREVENT + 1
pygame.time.set_timer(EVENT_NEW_COIN, 2000)

contador = 0
cont_grande = 0
count_coins = 10

# Direccion / Movimiento
move_up = False
move_right = False
move_down = False
move_left = False

# Fuente
fuente = pygame.font.SysFont(None, 48)

texto = fuente.render(f"Coins: {contador}", True, CUSTOM, BLACK)
rect_texto = texto.get_rect()
rect_texto.midtop = (width // 2, 30)   

# Creo el rectangulo
block = crear_bloque(randint(0, width - BLOCK_WIDTH), randint(0, height - BLOCK_WIDTH), BLOCK_WIDTH, BLOCK_HEIGHT, RED, radio= 25)

# Crear lista de coins
coins = []
load_coins_list(coins, count_coins)

# Variable de control
is_running = True

while is_running:
    clock.tick(FPS)
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
                new_coin = crear_bloque(event.pos[0], event.pos[1], size_coin, size_coin, WHITE, radio = size_coin // 2)
                new_coin["rect"].left -= size_coin // 2
                new_coin["rect"].top -= size_coin // 2
                coins.append(new_coin)
            if event.button == 3:
                block["rect"].center = (center_screen)
            
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
                load_coins_list(coins, count_coins)
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
    screen.fill(BLACK)
    
    for coin in coins:
        draw.rect(screen, coin["color"], coin["rect"], coin["borde"], coin["radio"])
    
    draw.rect(screen, block["color"], block["rect"], block["borde"], block["radio"])
    
    screen.blit(texto, rect_texto)
    
    # ---> Actualizar pantalla, puede ser flip o update()
    pygame.display.flip()
            
pygame.quit()
sys.exit()