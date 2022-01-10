from settings import *
import pygame
import math


class Player:
    def __init__(self, player_pos):
        self.x, self.y = player_pos
        self.angle = player_angle
        # collision settings
        self.side = 50
        self.rect = pygame.Rect(*player_pos, self.side, self.side)
        self.sensitivity = 0.001

    # Возвращаем позицию игрока по X, Y
    @property
    def pos(self):
        return self.x, self.y

    def detect_collision(self, dx, dy, coll_walls):
        next_rect = self.rect.copy()
        next_rect.move_ip(dx, dy)
        hit_indexes = next_rect.collidelistall(coll_walls)

        if len(hit_indexes):
            delta_x, delta_y = 0, 0
            for hit_index in hit_indexes:
                hit_rect = coll_walls[hit_index]
                if dx > 0:
                    delta_x += next_rect.right - hit_rect.left
                else:
                    delta_x += hit_rect.right - next_rect.left
                if dy > 0:
                    delta_y += next_rect.bottom - hit_rect.top
                else:
                    delta_y += hit_rect.bottom - next_rect.top
            if abs(delta_x - delta_y) < 10:
                dx, dy = 0, 0
            elif delta_x > delta_y:
                dy = 0
            elif delta_y > delta_x:
                dx = 0
        self.x += dx
        self.y += dy

    def movement(self, coll_walls, drawing=None):
        # self.keys_control(drawing)
        self.mouse_control()
        self.rect.center = self.x, self.y
        self.coll_walls = coll_walls

        # # Отслеживаем нажатые клавиши и меняем значение отрибутов
        # # Движимся относительно линии взгляда
        # def keys_control(self, drawing=None):
        #     global animation_hands_counter
        #     self.sensitivity = 0.00001

        animation_hands = False
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        # if keys[pygame.K_ESCAPE]:
        #     exit()
        if keys[pygame.K_w]:
            dx = player_speed * cos_a
            dy = player_speed * sin_a
            animation_hands = True
            self.detect_collision(dx, dy, self.coll_walls)
        if keys[pygame.K_s]:
            dx = -player_speed * cos_a
            dy = -player_speed * sin_a
            self.detect_collision(dx, dy, self.coll_walls)
        if keys[pygame.K_a]:
            dx = player_speed * sin_a
            dy = -player_speed * cos_a
            self.detect_collision(dx, dy, self.coll_walls)
        if keys[pygame.K_d]:
            dx = -player_speed * sin_a
            dy = player_speed * cos_a
            self.detect_collision(dx, dy, self.coll_walls)
        # if animation_hands and drawing:
        #     self.sensitivity *= 5

        # animation_hands_counter = drawing.anim(anim__, 1, animation_hands_counter)

    def mouse_control(self):
        if pygame.mouse.get_focused():
            difference = pygame.mouse.get_pos()[0] - HALF_WIDTH
            pygame.mouse.set_pos((HALF_WIDTH, HALF_HEIGHT))
            self.angle += difference * self.sensitivity
