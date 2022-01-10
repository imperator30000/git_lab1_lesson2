import map
from main_menu import *
from player import Player
from drawing import *
from ray_castting import ray_casting_walls
import settings
from random import choice
import os
from generation_lab import Maze


class Game:
    def __init__(self, MAZE=None):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        self.save_minimap_setting = []
        self.collision_walls = []
        self.world_map = []
        self.MAZE = MAZE
        if self.MAZE is None:
            self.MAZE = Maze(RADIUS)
        self.MAZE.make_maze()

        self.player_pos, self.game_map, self.win_pos = self.MAZE.info()
        self.player_pos = (self.player_pos[0] * 100 + 50, self.player_pos[1] * 100 + 50)
        self.win_pos = (self.win_pos[0] * 100, self.win_pos[1] * 100)

        self.world_map, self.collision_walls, self.WORLD_WIDTH, self.WORLD_HEIGHT = map.create_map(self.game_map)
        self.player = Player(self.player_pos)  # Игрок
        self.clock = pygame.time.Clock()  # Клас для определениея количества кадров в секунду
        self.drawing = Drawing(self.screen, self.clock, self.game_map, self.MAZE)

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

            self.player.movement(self.collision_walls, self.drawing)  # Ходьба
            # Обновляем экран на каждой итэрации
            pygame.display.flip()
            # Черный фон
            self.screen.fill(BLACK)
            # Рисуем землю и небо
            self.drawing.background()
            walls = ray_casting_walls(self.player, self.drawing.textures, self.world_map, self.WORLD_WIDTH,
                                      self.WORLD_HEIGHT)
            # Рисуем стены
            self.drawing.world(walls)
            # minimap
            # print(self.save_minimap_setting)
            self.drawing.minimap(self.player.pos, self.player.angle, self.save_minimap_setting)
            # self.save_minimap_setting = []
            # print(self.drawing.minimap_fill_quat())
            # счётчик фпсD
            self.drawing.fps(self.clock)
            self.drawing.chek_win(self.player.pos)
            if keys[pygame.K_m]:
                self.all_update()
            self.clock.tick()

    def all_update(self):
        self.MAZE.update_sek(0)
        game = Game(self.MAZE)
        game.run()

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
btn_pause.fun = win_game.run
win_menu.run()
