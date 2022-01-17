from settings import *
from random import randrange
import pygame
from math import pi
import datetime


class Drawing:
    def __init__(self, obj):
        self.obj = obj
        self.time_now = time_now
        self.setting_time = self.time_now
        self.count_time = count_time
        self.flag = True
        self.Name = Name
        self.sc = obj.screen
        self.clock = obj.clock
        self.game_map = obj.game_map
        self.MAZE = obj.MAZE
        self.font_win = pygame.font.SysFont("Arial", 144)
        self.font = pygame.font.SysFont("Arial", 36, bold=True)
        self.textures = {1: SELECTED_TEXTURES[0].convert(),
                         9: SELECTED_TEXTURES[0].convert()
                         }
        self.map = [[0 for g in range(len(obj.game_map))] for i in range(len(obj.game_map))]
        self.map_arr = [[], [], [], [], []]
        start = obj.radius - 3
        for i in range(7):
            for g in range(7):
                self.map[start + i][start + g] = 1
                self.map_arr[self.MAZE.check_quat(start + g, start + i)].append((start + g, start + i))



    def background(self):
        # Рисуем землю и небо
        pygame.draw.rect(self.sc, SKYBLUE, (0, 0, WIDTH, HALF_HEIGHT))
        pygame.draw.rect(self.sc, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, world_objects):
        for obj in sorted(world_objects, key=lambda n: n[0], reverse=True):
            if obj[0]:
                i, object, object_pos = obj
                self.sc.blit(object, object_pos)

    def time_clock(self, game):
        # таймер
        self.time_now -= 1
        display_time = str(self.time_now)
        if int(display_time) <= zero:
            game.all_update()
            self.count_time += 1
            time_now = self.setting_time
            display_time = str(time_now)
        if len(display_time) >= 5:
            display_time = str(int(display_time[:-2]) // 60) + ":" + str(
                int(display_time[:-2]) % 60) + ":" + display_time[-2:]
        elif len(display_time) >= 3:
            display_time = display_time[:-2] + ":" + display_time[-2:]
        else:
            display_time = "00" + ":" + display_time[-2:]
        display_time = "Update: " + display_time
        render = self.font.render(display_time, 0, BLACK)
        self.sc.blit(render, TIME_POS)

    def fps(self, clock):
        # Счётчик кадров
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, RED)
        self.sc.blit(render, FPS_POS)

    def chek_win(self, player_pos, time):
        if player_pos[0] < 0:
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                self.win(time)

    def win(self, time):
        render = self.font_win.render("YOU WIN", 1, (randrange(0, 255), randrange(0, 255), randrange(0, 255)))
        rect = pygame.Rect(0, 0, 1000, 300)
        rect.center = HALF_WIDTH, HALF_HEIGHT
        pygame.draw.rect(self.sc, BLACK, rect, border_radius=50)
        self.sc.blit(render, (rect.centerx - 430, rect.centery - 140))
        pygame.display.flip()
        if self.flag:
            set_time = str(datetime.datetime.now() - time)
            set_time = set_time[:set_time.index(".")].split(":")
            # print(datetime.timedelta(hours=int(set_time[0]), minutes=int(set_time[1]), seconds=int(set_time[2])))
            # print(datetime.timedelta(hours=0, minutes=count_time * setting_time // 100 // 60,
            #                          seconds=count_time * setting_time // 100 % 60))
            game_time = datetime.timedelta(hours=int(set_time[0]), minutes=int(set_time[1]), seconds=int(set_time[2]))
            update_time = datetime.timedelta(hours=0, minutes=self.count_time * self.setting_time // 100 // 60,
                                             seconds=self.count_time * self.setting_time // 100 % 60)
            self.flag = False
            a = cur.execute(f"""SELECT ID_Player
                            FROM players
                            WHERE players.Name = "{Name[0]}"
                            """).fetchall()
            print(a)
            con.execute(f"INSERT INTO records VALUES('{int(a[0][0])}', '{ RADIUS}', '{game_time + update_time}')")
            con.commit()
            self.obj.window_win.objs['Time'].text_ = str(game_time + update_time)
            self.obj.window_win.objs['Time'].update_text()
            self.obj.window_win.objs['Radius'].text_ = str(self.obj.radius)
            self.obj.window_win.objs['Radius'].update_text()

            self.obj.win_run()
            self.obj.pause_run() #self.obj.win_run() когда будет готово окно победы

        self.clock.tick(15)

    def minimap(self, player_pos, angel, m=tuple()):
        quat = self.minimap_fill_quat()
        # отрисовка миникарты
        x, y = player_pos
        x //= 100
        y //= 100
        x = int(x)
        y = int(y)
        x_map, y_map = 0, 0
        # print(*self.MAZE.maze, sep='\n')
        if tuple([x, y]) not in self.map_arr[self.MAZE.check_quat(x, y)] and \
                not self.MAZE.maze[y][x] or x == self.MAZE.r and \
                y in (self.MAZE.r - self.MAZE.k, self.MAZE.r - self.MAZE.k + 1):
            self.map[int(y)][int(x)] = 1
            if tuple([x, y]) not in self.MAZE.line()[-1]:
                self.map_arr[self.MAZE.check_quat(x, y)].append((x, y))
        n = 15
        k = 10
        pygame.draw.rect(self.sc, (0, 0, 0),
                         (x_map, y_map, (n + 2) * k, (n + 2) * k))

        for i in range(n):
            for g in range(n):
                col = (100, 100, 100)
                try:
                    if self.map[y + i - n // 2][x + g - n // 2] and y + i - n // 2 > 0 and x + g - n // 2 > 0:
                        if self.MAZE.check_quat(x + g - n // 2, y + i - n // 2) in quat:
                            col = (255, 255, 255)
                        pygame.draw.rect(self.sc, col,
                                         (x_map + k + g * k, y_map + k + i * k, k, k))
                except IndexError:
                    pass

        # ug = 360 - ((angel - 0.5) // (pi / 2) + 2) % 4 * 90
        ug = - 90 - angel * 180 / pi
        self.sc.blit(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('img/kur.png'), (k, k)), ug),
                     tuple([12 * k - n * 2 - k, 12 * k - n * 2 - k]))

    def minimap_clear_quat(self, num):
        self.map_arr[num].clear()
        for i in range(len(self.map)):
            for g in range(len(self.map[i])):
                if self.MAZE.check_quat(g, i, True, walls=True) == num:
                    self.map[i][g] = 0
        # if not num:
        #     self.map[self.MAZE.r - self.MAZE.k][self.MAZE.r] = 0
        #     self.map[self.MAZE.r - self.MAZE.k + 1][self.MAZE.r] = 0

    def minimap_fill_quat(self):
        arr = []
        # print(sorted(self.map_arr[0]),sorted(self.MAZE.maze_sekt[0].road), sep='\n')
        for i in range(4):
            if sorted(self.map_arr[i]) == sorted(self.MAZE.maze_sekt[i].road):
                # print('ok')
                arr.append(i)

        return arr

    # def anim(self, arr, speed, counter=0, name=0, x=0, y=0):
    #     obj = arr[0]
    #     if counter < speed:
    #         counter += 1
    #     else:
    #         arr.rotate()
    #         counter = 0
    #     self.screen.blit(obj, (0, 0))
    #
    #     return counter
