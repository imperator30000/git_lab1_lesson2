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

