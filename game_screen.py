import pygame
from config import FPS, WIDTH, HEIGHT, BLACK
from assets import carrega_arquivos
import random

def game_screen(window):
    clock = pygame.time.Clock()

    dicionario_de_arquivos = carrega_arquivos()

    DONE = 0
    PLAYING = 1
    WIN = 2
    estado_jogo = PLAYING

    N = 4
    #etapa 1
    def criar_quadrados_memoria(N):
        if N % 2 != 0:
            raise ValueError("N deve ser um número par para garantir pares de cores_quadrados")

        cores_quadrados = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
                 (255, 0, 255), (0, 255, 255), (128, 0, 0), (0, 128, 0),
                 ]

        cores_quadrados *= 2
        random.shuffle(cores_quadrados)

        quadrados = []
        #etapa 6
        for i in range(N):
            for j in range(N):
                x = WIDTH // 2 - (N * 150) // 2 + i * 150
                y = HEIGHT // 2 - (N * 150) // 2 + j * 150
                lado = 140
                revelado = False
                cor = cores_quadrados.pop()  # Removendo a cor da lista
                quadrado = {'x': x, 'y': y, 'lado': lado, 'cor': cor, 'revelado': revelado}
                quadrados.append(quadrado)

        return quadrados

    quadrados_memoria = criar_quadrados_memoria(N)
    revelado = []

    while estado_jogo != DONE:
        clock.tick(FPS)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                estado_jogo = DONE
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos_mouse = pygame.mouse.get_pos()
                for quadrado in quadrados_memoria:
                    if not quadrado['revelado']:
                        if colisao_ponto_quadrado(pos_mouse[0], pos_mouse[1],
                                                  quadrado['x'], quadrado['y'],
                                                  quadrado['lado'], quadrado['lado']):
                            quadrado['revelado'] = True
                            revelado.append(quadrado)

                            if len(revelado) == 2:
                                pygame.time.wait(500)  # Aguarda 0.5 segundo antes de esconder as cartas
                                if revelado[0]['cor'] == revelado[1]['cor']:
                                    quadrados_memoria.remove(revelado[0])
                                    quadrados_memoria.remove(revelado[1])
                                else:
                                    revelado[0]['revelado'] = False
                                    revelado[1]['revelado'] = False
                                revelado = []

        window.fill(BLACK)
        #etapa 2
        for quadrado in quadrados_memoria:
            if quadrado['revelado']:
                pygame.draw.rect(window, quadrado['cor'], (quadrado['x'], quadrado['y'], quadrado['lado'], quadrado['lado']))
            else:
                pygame.draw.rect(window, (255, 255, 255), (quadrado['x'], quadrado['y'], quadrado['lado'], quadrado['lado']))

        pygame.display.update()

        # etapa 5
        if not quadrados_memoria and estado_jogo == PLAYING:
            estado_jogo = WIN

        if estado_jogo == WIN:
            # Tela de Parabéns
            font = pygame.font.Font(None, 36)
            texto = font.render("Parabéns, você ganhou!", True, (255, 255, 255))
            window.blit(texto, (WIDTH // 2 - texto.get_width() // 2, HEIGHT // 2 - texto.get_height() // 2))
            pygame.display.update()
            pygame.time.wait(3000)  # Aguarda 3 segundos antes de encerrar o jogo
            estado_jogo = DONE

    pygame.quit()

    return estado_jogo
#etapa 3
def colisao_ponto_quadrado(x_ponto, y_ponto, x_quadrado, y_quadrado, largura_quadrado, altura_quadrado):
    if x_quadrado <= x_ponto <= x_quadrado + largura_quadrado and y_quadrado <= y_ponto <= y_quadrado + altura_quadrado:
        return True
    else:
        return False
