import datetime
import map
from player import Player
from drawing import *
from ray_castting import ray_casting_walls

from generation_lab import Maze


class Game:
    def __init__(self, radius=RADIUS):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.save_minimap_setting = []
        self.collision_walls = []
        self.world_map = []
        self.pause_run = lambda: 1
        self.radius = radius
        self.MAZE = None

        self.player_pos, self.game_map, self.win_pos = None, None, None
        self.win_pos = None

        self.world_map, self.collision_walls, self.WORLD_WIDTH, self.WORLD_HEIGHT = None, None, None, None
        self.player = None  # Игрок
        self.clock = None  # Клас для определениея количества кадров в секунду
        self.drawing = None
        self.new_maze(self.radius)

        # self.MAZE = Maze(radius)
        #
        # self.MAZE.make_maze()
        #
        # self.player_pos, self.game_map, self.win_pos = self.MAZE.info()
        # self.player_pos = (self.player_pos[0] * 100 + 50, self.player_pos[1] * 100 + 50)
        # self.win_pos = (self.win_pos[0] * 100, self.win_pos[1] * 100)
        #
        # self.world_map, self.collision_walls, self.WORLD_WIDTH, self.WORLD_HEIGHT = map.create_map(self.game_map)
        # self.player = Player(self.player_pos)  # Игрок
        # self.clock = pygame.time.Clock()  # Клас для определениея количества кадров в секунду
        # self.drawing = Drawing(self)

    def new_maze(self, radius):
        self.MAZE = Maze(radius)
        self.radius = radius

        self.MAZE.make_maze()

        self.player_pos, self.game_map, self.win_pos = self.MAZE.info()
        self.player_pos = (self.player_pos[0] * 100 + 50, self.player_pos[1] * 100 + 50)
        self.win_pos = (self.win_pos[0] * 100, self.win_pos[1] * 100)

        self.world_map, self.collision_walls, self.WORLD_WIDTH, self.WORLD_HEIGHT = map.create_map(self.game_map)
        self.player = Player(self.player_pos)  # Игрок
        self.clock = pygame.time.Clock()  # Клас для определениея количества кадров в секунду
        self.drawing = Drawing(self)

    def run(self):
        now = datetime.datetime.now()
        pygame.mouse.set_visible(False)
        while True:
            # Проверка на закрытие программы
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.pause_run()

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
            self.drawing.chek_win(self.player.pos, now)
            self.drawing.time_clock(self)
            if keys[pygame.K_m]:
                self.all_update()
            self.clock.tick()

    def all_update(self):
        global quat_update

        player_quat = self.MAZE.check_quat(int(self.player.pos[0]//100), int(self.player.pos[1]//100), walls=True)
        # print(quat_update, player_quat)
        new_pos = player_quat == quat_update

        self.MAZE.update_sek(quat_update)
        self.drawing.minimap_clear_quat(quat_update)
        _, self.game_map, __ = self.MAZE.info()
        if new_pos:
            self.player_pos, self.win_pos = _, __
            self.player_pos = (self.player_pos[0] * 100 + 50, self.player_pos[1] * 100 + 50)
            self.win_pos = (self.win_pos[0] * 100, self.win_pos[1] * 100)
            self.player = Player(self.player_pos)

        self.world_map, self.collision_walls, self.WORLD_WIDTH, self.WORLD_HEIGHT = map.create_map(self.game_map)
        self.clock = pygame.time.Clock()  # Клас для определениея количества кадров в секунду
        self.player.steping = True
        quat_update = (quat_update + 1) % 4
        pygame.time.wait(100)

        # self.run()

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