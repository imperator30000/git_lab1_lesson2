import pygame
from settings import *
from player import Player
from drawing import Drawing

# Основное рабочее окно
pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()  # Клас для определениея количества кадров в секунду
player = Player()  # Игрок
drawing = Drawing(sc, clock)
# Основной цикл программы
while True:
    # Проверка на закрытие программы
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    player.movement()  # Ходьба
    # Черный фон
    sc.fill(BLACK)
    # Рисуем землю и небо
    drawing.background()
    # Рисуем стены
    drawing.world(player.pos, player.angle)
    # счётчик фпсD
    drawing.fps(clock)
    c = anim(anim__, sc, c)
    drawing.chek_win(player.pos)

    # Обновляем экран на каждой итэрации
    pygame.display.flip()
    clock.tick()
