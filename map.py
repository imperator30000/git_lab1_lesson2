from settings import *
import pygame
from numba.core import types
from numba.typed import Dict
from numba import int64


# карта
# Для определения правильной длины луча\
# print(*MAZE.maze, sep='\n', end='\n-----\n')
# print(*game_map, sep='\n', end='\n-----\n')
def create_map(game_map):
    WORLD_WIDTH = len(game_map[0]) * TILE
    WORLD_HEIGHT = len(game_map) * TILE
    collision_walls = []
    world_map = Dict.empty(key_type=types.UniTuple(int64, 2), value_type=int64)
    for j, row in enumerate(game_map):
        for i, char in enumerate(row):
            if char:
                collision_walls.append(pygame.Rect(i * TILE, j * TILE, TILE, TILE))
                if char == 9:
                    world_map[(i * TILE, j * TILE)] = 9
                elif char == 1:
                    world_map[(i * TILE, j * TILE)] = 1
    return world_map, collision_walls, WORLD_WIDTH, WORLD_HEIGHT
