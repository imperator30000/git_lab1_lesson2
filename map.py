from settings import *

# Карта

# карта
world_map = {}

for j, row in enumerate(game_map):
    for i, char in enumerate(row):
        if char != 0:
            if char == 9:
                world_map[(i * TILE, j * TILE)] = "9"
            elif char == 1:
                world_map[(i * TILE, j * TILE)] = "1"

