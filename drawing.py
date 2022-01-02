import pygame
from settings import *
from ray_castting import ray_casting


class Drawing:
    def __init__(self, sc):
        self.sc = sc
        self.font = pygame.font.SysFont("Arial", 36, bold=True)
        self.textures = {"1": pygame.image.load("images/1.png").convert(),
                         "9": pygame.image.load("images/2.png").convert()
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
