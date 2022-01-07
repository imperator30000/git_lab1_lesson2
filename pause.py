from win_menu import Obj, Window
import pygame as pg

win_pause = Window((1200, 800), pg.image.load('img/back_.png'), 'name1')
btn_pause = Obj(pg.image.load('img/brick.png'), (310, 350), (250, 100), 'pause', 'btn', 'pause')
btn_restart = Obj(pg.image.load('img/brick.png'), (650, 350), (250, 100), 'restart', 'btn', 'restart')
win_pause.add_obj(btn_pause)
win_pause.add_obj(btn_restart)
# win_pause.run()
