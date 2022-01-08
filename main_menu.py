from win_menu import Obj, Window
import pygame as pg
from Shader import PyShader
from maze_back import MazeBack
#, pg.image.load('img/back_.png'), 'name1'
back = MazeBack
# back = PyShader
win_pause = Window((1200, 800), back)
btn_pause = Obj(pg.image.load('img/brick.png'), (310, 350), (250, 100), 'pause', 'btn', 'pause')
btn_restart = Obj(pg.image.load('img/brick.png'), (650, 350), (250, 100), 'restart', 'btn', 'restart')
win_pause.add_obj(btn_pause)
win_pause.add_obj(btn_restart)


back = PyShader
win_menu= Window((1200, 800), back)
btn_play = Obj(pg.image.load('img/brick_.png'), (310, 450), (270, 100), 'play', 'btn', 'play', fun=win_pause.run)
btn_settings = Obj(pg.image.load('img/brick_.png'), (630, 450), (270, 100), 'settings', 'btn', 'settings', 60)
btn_spin = Obj(pg.image.load('img/brick_.png'), (100, 100), (100, 100), 'spin', 'spin', '11', 60)

btn_title = Obj(pg.image.load('img/brick_.png'), (310, 210), (590, 200), 'Maze', 'title', 'Maze', 100)
win_menu.add_obj(btn_spin)
win_menu.add_obj(btn_play)
win_menu.add_obj(btn_settings)
win_menu.add_obj(btn_title)
btn_restart.fun=win_menu.run
win_menu.run()
