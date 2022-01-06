import pygame
from player import Player
from drawing import *
from ray_castting import ray_casting_walls

# Основное рабочее окно
pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()  # Клас для определениея количества кадров в секунду
player = Player()  # Игрок
drawing = Drawing(sc, clock)
# Основной цикл программы
# MAZE.update_sek(1)

while True:
    # Проверка на закрытие программы
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    player.movement(drawing)  # Ходьба
    # Обновляем экран на каждой итэрации
    pygame.display.flip()
    # Черный фон
    sc.fill(BLACK)
    # Рисуем землю и небо
    drawing.background()
    walls = ray_casting_walls(player, drawing.textures)
    # Рисуем стены
    drawing.world(walls)
    # minimap
    drawing.minimap(player.pos, player.angle)
    print(drawing.minimap_fill_quat())
    # счётчик фпсD
    drawing.fps(clock)
    drawing.chek_win(player.pos)

    clock.tick()
