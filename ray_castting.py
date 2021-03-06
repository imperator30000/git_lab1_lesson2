import pygame
from settings import *
import math
from numba import njit


@njit(fastmath=True)
def mapping(a, b):
    return (a // TILE) * TILE, (b // TILE) * TILE


@njit(fastmath=True)
def ray_casting(player_pos, player_angle, world_map, WORLD_WIDHT, WORLD_HEIGHT):
    casted_walls = []
    texture_v, texture_h = 1, 1
    ox, oy = player_pos
    xm, ym = mapping(ox, oy)
    cur_angle = player_angle - HALF_FOV
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)

        # Алгоритм просчёта расстояния до стенки
        # Вертикаль
        x, dx = (xm + TILE, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, WORLD_WIDHT, TILE):
            depth_v = (x - ox) / cos_a
            yv = oy + depth_v * sin_a
            tile_v = mapping(x + dx, yv)
            if tile_v in world_map:
                texture_v = world_map[tile_v]
                break
            x += dx * TILE
        # Горизонталь
        y, dy = (ym + TILE, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, WORLD_HEIGHT, TILE):
            depth_h = (y - oy) / sin_a
            xh = ox + depth_h * cos_a
            tile_h = mapping(xh, y + dy)
            if tile_h in world_map:
                texture_h = world_map[tile_h]
                break
            y += dy * TILE

        # выборка
        depth, offset, texture = (depth_v, yv, texture_v) if depth_v < depth_h else (depth_h, xh, texture_h)
        offset = int(offset) % TILE
        depth *= math.cos(player_angle - cur_angle)
        depth = max(depth, 0.000005)
        proj_hight = min(int(PROJ_COEFF / depth), 2 * PENTA_HIGHT)  # Высота проекции стены
        casted_walls.append((depth, offset, proj_hight, texture))
        # Измениение угла для нового луча
        cur_angle += DELTA_ANGLE
    return casted_walls


def ray_casting_walls(player, textures, world_map, WORLD_WIDTH, WORLD_HEIGHT):
    casted_walls = ray_casting(player.pos, player.angle, world_map, WORLD_WIDTH, WORLD_HEIGHT)
    walls = []
    for ray, casted_values in enumerate(casted_walls):
        depth, offset, proj_hight, texture = casted_values
        wall_column = textures[texture].subsurface(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_HEIGHT)
        wall_column = pygame.transform.scale(wall_column, (SCALE, proj_hight))
        wall_pos = (ray * SCALE, HALF_HEIGHT - proj_hight // 2)
        walls.append((depth, wall_column, wall_pos))
    return walls
