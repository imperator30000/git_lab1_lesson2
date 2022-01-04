import pygame
from settings import *
from ray_castting import ray_casting
import sys
from random import randrange


class Drawing:
    def __init__(self, sc, clock):
        self.sc = sc
        self.clock = clock
        self.font_win = pygame.font.SysFont("Arial", 144)
        self.font = pygame.font.SysFont("Arial", 36, bold=True)
        self.textures = {1: pygame.image.load("images/1.png").convert(),
                         9: pygame.image.load("images/2.png").convert()
                         }
        self.map = [[0 for g in range(len(game_map))] for i in range(len(game_map))]
        start = RADIUS - 3
        for i in range(7):
            for g in range(7):
                self.map[start + i][start + g] = 1

    def background(self):
        # Рисуем землю и небо
        pygame.draw.rect(self.sc, SKYBLUE, (0, 0, WIDTH, HALF_HEIGHT))
        pygame.draw.rect(self.sc, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, player_pos, player_angle):
        # Отрисовка стен
        ray_casting(self.sc, player_pos, player_angle, self.textures)

    def fps(self, clock):
        # Счётчик кадров
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, RED)
        self.sc.blit(render, FPS_POS)

    def chek_win(self, player_pos):
        print(player_pos, win_pos)
        if player_pos[0] < 0:
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                self.win()

    def win(self):
        render = self.font_win.render("YOU WIN", 1, (randrange(0, 255), randrange(0, 255), randrange(0, 255)))
        rect = pygame.Rect(0, 0, 1000, 300)
        rect.center = HALF_WIDTH, HALF_HEIGHT
        pygame.draw.rect(self.sc, BLACK, rect, border_radius=50)
        self.sc.blit(render, (rect.centerx - 430, rect.centery - 140))
        pygame.display.flip()
        self.clock.tick(15)

    def minimap(self, player_pos):
        # отрисовка миникарты
        x, y = player_pos
        x //= 100
        y //= 100
        x = int(x)
        y = int(y)
        x_map, y_map = 0, 0
        self.map[int(y)][int(x)] = 1
        n = 15
        k = 10
        pygame.draw.rect(self.sc, (0, 0, 0),
                         (x_map, y_map, (n + 2) * k, (n + 2) * k))
        for i in range(n):
            for g in range(n):
                try:

                    if self.map[y + i - n // 2][x + g - n // 2] and y + i - n // 2 > 0 and x + g - n // 2 > 0:
                        pygame.draw.rect(self.sc, (100, 100, 100),
                                         (x_map + k + g * k, y_map + k + i * k, k, k))
                except IndexError:
                    pass
        pygame.draw.circle(self.sc, (100, 255, 100),
                           tuple([RADIUS * k - n * 2 - (k // 2), RADIUS * k - n * 2 - (k // 2)]), k // 2)

    def anim(self, arr, counter=0, name=0, x=0, y=0):
        if counter > len(arr) ** 2 - len(arr):
            counter = 0
        if name:
            self.sc.blit(arr[counter // len(arr)], (x - int(arr[counter // len(arr)].get_rect()[2]), y))
        else:
            self.sc.blit(arr[counter // len(arr)], (x, y))
        print(counter // len(arr))
        counter += len(arr) // 3


        return counter


