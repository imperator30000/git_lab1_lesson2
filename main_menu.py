from win_menu import Obj, Window
import pygame as pg
from Shader import PyShader
from maze_back import MazeBack

# , pg.image.load('img/back_.png'), 'name1'


back = MazeBack
back = PyShader
win_pause = Window((1200, 800), back)
btn_pause = Obj(pg.image.load('img/brick.png'), (310, 350), (250, 100), 'pause', 'btn', 'pause')
btn_restart = Obj(pg.image.load('img/brick.png'), (650, 350), (250, 100), 'restart', 'btn', 'restart')
win_pause.add_obj(btn_pause)
win_pause.add_obj(btn_restart)

# back = PyShader
win_menu = Window((1200, 800), back)
btn_play = Obj(pg.image.load('img/brick_.png'), (310, 450), (270, 100), 'play', 'btn', 'play', fun=win_pause.run)
btn_settings = Obj(pg.image.load('img/brick_.png'), (630, 450), (270, 100), 'settings', 'btn', 'settings', 60)

btn_title = Obj(pg.image.load('img/brick_.png'), (310, 210), (590, 200), 'Maze', 'title', 'Maze', 100)
win_menu.add_obj(btn_play)
win_menu.add_obj(btn_settings)
win_menu.add_obj(btn_title)
btn_restart.fun = win_menu.run



win_castom_mode = Window((1200, 800), back)
title_castom_mode = Obj(pg.image.load('img/brick_.png'), (50, 50), (300, 100), 'Castom mode', 'title', 'Castom mode',
                        50, ok=150)
win_castom_mode.add_obj(title_castom_mode)
title_hard_mode = Obj(pg.image.load('img/brick_.png'), (50, 200), (300, 100), 'Hard mode', 'btn', 'Hard mode', 50)
win_castom_mode.add_obj(title_hard_mode)
title_play = Obj(pg.image.load('img/brick_.png'), (50, 350), (300, 100), 'Play', 'btn', 'Play')
win_castom_mode.add_obj(title_play)
title_menu = Obj(pg.image.load('img/brick_.png'), (50, 650), (300, 100), 'Menu', 'btn', 'Menu')
win_castom_mode.add_obj(title_menu)
title_radius = Obj(pg.image.load('img/brick_.png'), (850, 50), (300, 100), 'Radius', 'title', 'Radius')
win_castom_mode.add_obj(title_radius)
title_spin_radius = Obj(pg.image.load('img/brick_.png'), (950, 200), (100, 100), 'Spin radius', 'spin', '11')
win_castom_mode.add_obj(title_spin_radius, ['Radius'])
title_time = Obj(pg.image.load('img/brick_.png'), (850, 350), (300, 100), 'Time update', 'title', 'Time update',  50)
win_castom_mode.add_obj(title_time)
title_spin_time = Obj(pg.image.load('img/brick_.png'), (950, 500), (100, 100), 'Spin time', 'spin', '900',40,step_spin=10,
                      min_max=(100, 1000))
win_castom_mode.add_obj(title_spin_time, ['Time update'])




win_hard_mode = Window((1200, 800), back)
title_hard_mode.fun = win_hard_mode.run
title_castom_mode = Obj(pg.image.load('img/brick_.png'), (50, 50), (300, 100), 'Castom mode', 'btn', 'Castom mode',
                        50, fun=win_castom_mode.run)
win_hard_mode.add_obj(title_castom_mode)
title_hard_mode = Obj(pg.image.load('img/brick_.png'), (50, 200), (300, 100), 'Hard mode', 'title', 'Hard mode', 50, ok=150)
win_hard_mode.add_obj(title_hard_mode)
title_play_ = Obj(pg.image.load('img/brick_.png'), (50, 350), (300, 100), 'Play', 'btn', 'Play', fun=win_pause.run)
win_hard_mode.add_obj(title_play_)
title_menu = Obj(pg.image.load('img/brick_.png'), (50, 650), (300, 100), 'Menu', 'btn', 'Menu')
win_hard_mode.add_obj(title_menu)
title_radius = Obj(pg.image.load('img/brick_.png'), (850, 50), (300, 100), 'Hard', 'title', 'Hard')
win_hard_mode.add_obj(title_radius)
title_spin_radius = Obj(pg.image.load('img/brick_.png'), (950, 200), (100, 100), 'Spin hard', 'spin', '1', min_max=(1, 20))
win_hard_mode.add_obj(title_spin_radius, ['Hard'])
btn_play.fun = win_hard_mode.run

win_menu.run()