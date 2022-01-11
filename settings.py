# game settings
import math
from Shader import PyShader
from maze_back import MazeBack
# Разрешение окна
WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
PENTA_HIGHT = 5 * HEIGHT

# Количество кадров
FPS = 45
# Размер квадрата карты
RADIUS = 11

TILE = 100
FPS_POS = (WIDTH - 65, 5)

# player settings
# player_pos = (HALF_WIDTH, HALF_HEIGHT)  # Позиция игрока
player_angle = 4.7  # Направление взгляда
player_speed = 5  # Скорость перемещения игрока

# ray casting settings
FOV = math.pi / 3  # Угол обзора
HALF_FOV = FOV / 2
NUM_RAYS = 300  # Количество исускаемых лучей
MAX_DEPTH = 800  # Далность прорисовки
DELTA_ANGLE = FOV / NUM_RAYS  # Угол между лучами
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))  # Расстояние до стены которую должен видеть пользователь
PROJ_COEFF = 3 * DIST * TILE  # Размер стены которую видит пользователь
SCALE = WIDTH // NUM_RAYS  # Масштаб

# texture (1200 * 1200)
TEXTURE_WIDTH = 1200
TEXTURE_HEIGHT = 1200
TEXTURE_SCALE = TEXTURE_WIDTH // TILE

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 80, 0)
BLUE = (0, 0, 225)
DARKGRAY = (40, 40, 40)
PURPLE = (120, 0, 120)
SKYBLUE = (0, 186, 255)
YELLOW = (220, 220, 0)

# anim__ = deque(
#     [pygame.transform.scale(pygame.image.load(f'images/анимация/{i}.png'), (WIDTH, HEIGHT)) for i in range(21)])
# animation_hands = True
# animation_hands_counter = 0
#
# c = 0
# меню
MENU_BACK_dict = {'Maze 2D': MazeBack, 'Maze 3D': PyShader}
MENU_BACK = MENU_BACK_dict['Maze 2D']