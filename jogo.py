# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
from config import WIDTH, HEIGHT, INIT, GAME, QUIT
from init_screen import init_screen
from game_screen import game_screen

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jogo da Memoria')

estado_jogo = INIT
while estado_jogo != QUIT:
    if estado_jogo == INIT:
        estado_jogo = init_screen(window)
    elif estado_jogo == GAME:
        estado_jogo = game_screen(window)
    else:
        estado_jogo = QUIT

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

