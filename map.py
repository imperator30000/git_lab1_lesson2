from settings import *
import pygame
from numba.core import types
from numba.typed import Dict
from numba import int64

# карта
world_map = Dict.empty(key_type=types.UniTuple(int64, 2), value_type=int64)
collision_walls = []
# Для определения правильной длины луча
WORLD_WIDHT = len(game_map[0]) * TILE
WORLD_HEIGHT = len(game_map) * TILE
# print(*MAZE.maze, sep='\n', end='\n-----\n')
# print(*game_map, sep='\n', end='\n-----\n')
for j, row in enumerate(game_map):
    for i, char in enumerate(row):
        if char:
            collision_walls.append(pygame.Rect(i * TILE, j * TILE, TILE, TILE))
            if char == 9:
                world_map[(i * TILE, j * TILE)] = 9
            elif char == 1:
                world_map[(i * TILE, j * TILE)] = 1
