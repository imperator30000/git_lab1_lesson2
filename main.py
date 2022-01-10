from main_menu import *
from player import Player
from drawing import *
from ray_castting import ray_casting_walls



class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        self.clock = pygame.time.Clock()  # Клас для определениея количества кадров в секунду
        self.player = Player()  # Игрок
        self.drawing = Drawing(self.screen, self.clock)


    def run(self):
        pygame.mouse.set_visible(False)
        while True:
            # Проверка на закрытие программы
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                win_pause.run()

            self.player.movement(self.drawing)  # Ходьба
            # Обновляем экран на каждой итэрации
            pygame.display.flip()
            # Черный фон
            self.screen.fill(BLACK)
            # Рисуем землю и небо
            self.drawing.background()
            walls = ray_casting_walls(self.player, self.drawing.textures)
            # Рисуем стены
            self.drawing.world(walls)
            # minimap
            self.drawing.minimap(self.player.pos, self.player.angle)
            print(self.drawing.minimap_fill_quat())
            # счётчик фпсD
            self.drawing.fps(self.clock)
            self.drawing.chek_win(self.player.pos)

            self.clock.tick()

# # Основное рабочее окно
# pygame.init()
# sc = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.mouse.set_visible(False)
# clock = pygame.time.Clock()  # Клас для определениея количества кадров в секунду
# player = Player()  # Игрок
# drawing = Drawing(sc, clock)
# # Основной цикл программы
# # MAZE.update_sek(1)
#
# while True:
#     # Проверка на закрытие программы
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#
#     player.movement(drawing)  # Ходьба
#     # Обновляем экран на каждой итэрации
#     pygame.display.flip()
#     # Черный фон
#     sc.fill(BLACK)
#     # Рисуем землю и небо
#     drawing.background()
#     walls = ray_casting_walls(player, drawing.textures)
#     # Рисуем стены
#     drawing.world(walls)
#     # minimap
#     drawing.minimap(player.pos, player.angle)
#     print(drawing.minimap_fill_quat())
#     # счётчик фпсD
#     drawing.fps(clock)
#     drawing.chek_win(player.pos)
#
#     clock.tick()
win_game = Game()
title_play_.fun = win_game.run
win_menu.run()