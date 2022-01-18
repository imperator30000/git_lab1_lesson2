# game settings
import math
from Shader import PyShader
from maze_back import MazeBack
import pygame as pg
import sqlite3 as sq

pg.mixer.init(channels=2)
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
TIME_POS = (5, 170)

setting_time = time_now = 300 * 100
zero = 0
count_time = 0
quat_update = 0
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

Name = ['qw']
with sq.connect("GAME.db") as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS players (
        ID_Player INTEGER auto_increment primary key, 
        Name TEXT,
        Password TEXT
        )""")
con.commit()
with sq.connect("GAME.db") as con_2:
    cur_2 = con.cursor()
    cur_2.execute("""CREATE TABLE IF NOT EXISTS records (
        ID_player INTEGER, 
        Maze radius INTEGER,
        Time TEXT,
        FOREIGN KEY (ID_player) REFERENCES players (ID_Player)
        )""")
con_2.commit()
FLAG = True


def data_base(name, password):
    global Name
    cur = con.cursor()
    info = cur.execute('SELECT * FROM players WHERE Name=? and Password=?', (name, password))
    if info.fetchone() is None:
        print("Вас нету в базе")
        print("добавляю вас")
        con.execute("INSERT INTO records VALUES(?, ?, ?)",
                    (1, name, password))
        return False
    else:
        Name[0] = name
        return True


def logining_(name, password):
    global Name
    conn = sq.connect('GAME.db')
    cur_ = conn.cursor()
    info = cur_.execute(f'SELECT password FROM players WHERE Name="{name}" ').fetchall()
    if not len(info):
        ids = cur_.execute(f'SELECT [ID_Player] FROM players ').fetchall()
        try:
            id_ = max([i[0] for i in ids]) + 1
        except ValueError:
            id_ = 0
        cur_.execute(f"INSERT INTO players VALUES({id_}, '{name}', '{password}')")
        conn.commit()
        Name[0] = name
        return True
    if password == info[0][0]:
        Name[0] = name
        return True
    return False

#
# logining('Pivo', 'qwerty')
# logining('Pivo', 'qwerty1')
# logining('Pivo1', 'qwerty')
# меню
TEXTURES = {'Red brick': pg.image.load('images/2.png'), 'Grey brick': pg.image.load('images/1.png')}
SELECTED_TEXTURES = [TEXTURES['Grey brick']]
MENU_BACK_dict = {'Maze 2D': MazeBack, 'Maze 3D': PyShader}
MENU_BACK = MENU_BACK_dict['Maze 2D']
VOLUME = [0, 0.7, 1]
BACK_MUZ = pg.mixer.Sound('back_mus.wav')
CLICK_SOUND = pg.mixer.Sound("click.wav")
STEP_SOUND = pg.mixer.Sound('step.wav')
END_COUNT = pg.mixer.Sound('end.wav')
BACK_MUZ.set_volume(VOLUME[0])
CLICK_SOUND.set_volume(VOLUME[1])
STEP_SOUND.set_volume(VOLUME[2])
END_COUNT.set_volume(VOLUME[2])
STEP_SOUND.play(-1)
STEP_SOUND.stop()
