from win_menu import Obj, Window, InputBox
import pygame as pg
from settings import *
from main import Game

# регистрация/вход
win_login = Window((1200, 800), MENU_BACK)
win_login_input_login = InputBox(pg.image.load('img/brick_.png'), (80, 480), (500, 80), 'Login_input', 'btn',
                                 font_size=30)
win_login_input_password = InputBox(pg.image.load('img/brick_.png'), (620, 480), (500, 80), 'Password_input', 'btn',
                                    font_size=30)
win_login_title_maze = Obj(pg.image.load('img/brick_.png'), (310, 80), (590, 200), 'Maze', 'title', 'Maze', 100)
win_login_title_password = Obj(pg.image.load('img/brick_.png'), (620, 360), (500, 80), 'Password', 'title', 'Password')
win_login_title_login = Obj(pg.image.load('img/brick_.png'), (80, 360), (500, 80), 'login', 'title', 'login')
win_login_btn_play = Obj(pg.image.load('img/brick_.png'), (450, 640), (300, 80), 'Play', 'btn', 'Play')

win_login.add_obj(win_login_input_login)
win_login.add_obj(win_login_input_password)
win_login.add_obj(win_login_title_maze)
win_login.add_obj(win_login_title_password)
win_login.add_obj(win_login_title_login)
win_login.add_obj(win_login_btn_play)

# неверный пароль
win_invalid_password = Window((1200, 800), MENU_BACK)

win_invalid_password_title = Obj(pg.image.load('img/brick_.png'), (100, 80), (1000, 100), 'Invalid password', 'title',
                                 'An invalid password or an account with such a login exists', font_size=35)
win_invalid_password_btn_menu = Obj(pg.image.load('img/brick_.png'), (450, 640), (300, 80), 'Back', 'btn', 'Back')

win_invalid_password.add_obj(win_invalid_password_title)
win_invalid_password.add_obj(win_invalid_password_btn_menu)

# меню
win_menu = Window((1200, 800), MENU_BACK)

win_menu_btn_play = Obj(pg.image.load('img/brick_.png'), (310, 450), (270, 100), 'Play', 'btn', 'Play')
win_menu_btn_settings = Obj(pg.image.load('img/brick_.png'), (630, 450), (270, 100), 'settings', 'btn', 'settings', 60)
win_menu_title_title = Obj(pg.image.load('img/brick_.png'), (310, 210), (590, 200), 'Maze', 'title', 'Maze', 100)

win_menu.add_obj(win_menu_btn_play)
win_menu.add_obj(win_menu_btn_settings)
win_menu.add_obj(win_menu_title_title)

# кастомный режим
win_configurable_mode = Window((1200, 800), MENU_BACK)

win_configurable_mode_title_configurable_mode = Obj(pg.image.load('img/brick_.png'), (50, 50), (300, 100),
                                                    'Configurable mode', 'title',
                                                    'Configurable mode',
                                                    35, ok=150)
win_configurable_mode_btn_hard_mode = Obj(pg.image.load('img/brick_.png'), (50, 200), (300, 100), 'Hard mode', 'btn',
                                          'Hard mode', 50)
win_configurable_mode_btn_play = Obj(pg.image.load('img/brick_.png'), (50, 350), (300, 100), 'Play', 'btn', 'Play')
win_configurable_mode_btn_menu = Obj(pg.image.load('img/brick_.png'), (50, 650), (300, 100), 'Menu', 'btn', 'Menu')
win_configurable_mode_title_radius = Obj(pg.image.load('img/brick_.png'), (850, 50), (300, 100), 'Radius', 'title',
                                         'Radius')
win_configurable_mode_spin_radius = Obj(pg.image.load('img/brick_.png'), (950, 200), (100, 100), 'Spin radius', 'spin',
                                        '11')
win_configurable_mode_title_time = Obj(pg.image.load('img/brick_.png'), (850, 350), (300, 100), 'Time update', 'title',
                                       'Time update', 50)
win_configurable_mode_spin_time = Obj(pg.image.load('img/brick_.png'), (950, 500), (100, 100), 'Spin time', 'spin',
                                      '900', 40,
                                      step_spin=10,
                                      min_max=(100, 1000))

win_configurable_mode.add_obj(win_configurable_mode_title_configurable_mode)
win_configurable_mode.add_obj(win_configurable_mode_btn_hard_mode)
win_configurable_mode.add_obj(win_configurable_mode_btn_play)
win_configurable_mode.add_obj(win_configurable_mode_btn_menu)
win_configurable_mode.add_obj(win_configurable_mode_title_radius)
win_configurable_mode.add_obj(win_configurable_mode_spin_radius, ['Radius'])
win_configurable_mode.add_obj(win_configurable_mode_title_time)
win_configurable_mode.add_obj(win_configurable_mode_spin_time, ['Time update'])

# сложность
win_hard_mode = Window((1200, 800), MENU_BACK)

win_hard_mode_btn_castom_mode = Obj(pg.image.load('img/brick_.png'), (50, 50), (300, 100), 'Configurable mode', 'btn',
                                    'Configurable mode',
                                    35, fun=win_configurable_mode.run)
win_hard_mode_title_hard_mode = Obj(pg.image.load('img/brick_.png'), (50, 200), (300, 100), 'Hard mode', 'title',
                                    'Hard mode', 50,
                                    ok=150)
win_hard_mode_btn_play_ = Obj(pg.image.load('img/brick_.png'), (50, 350), (300, 100), 'Play', 'btn', 'Play')
win_hard_mode_btn_menu = Obj(pg.image.load('img/brick_.png'), (50, 650), (300, 100), 'Menu', 'btn', 'Menu')
win_hard_mode_title_radius = Obj(pg.image.load('img/brick_.png'), (850, 50), (300, 100), 'Hard', 'title', 'Hard')
win_hard_mode_spin_radius = Obj(pg.image.load('img/brick_.png'), (950, 200), (100, 100), 'Spin hard', 'spin', '1',
                                min_max=(1, 20))

win_hard_mode.add_obj(win_hard_mode_btn_castom_mode)
win_hard_mode.add_obj(win_hard_mode_title_hard_mode)
win_hard_mode.add_obj(win_hard_mode_btn_play_)
win_hard_mode.add_obj(win_hard_mode_btn_menu)
win_hard_mode.add_obj(win_hard_mode_title_radius)
win_hard_mode.add_obj(win_hard_mode_spin_radius, ['Hard'])

# пауза
win_pause = Window((1200, 800), MENU_BACK)

win_pause_btn_play = Obj(pg.image.load('img/brick_.png'), (120, 350), (240, 100), 'Play', 'btn', 'Play')
win_pause_btn_restart = Obj(pg.image.load('img/brick_.png'), (480, 350), (240, 100), 'Restart', 'btn', 'Restart')
win_pause_btn_menu = Obj(pg.image.load('img/brick_.png'), (840, 350), (240, 100), 'Menu', 'btn', 'Menu')

win_pause.add_obj(win_pause_btn_play)
win_pause.add_obj(win_pause_btn_restart)
win_pause.add_obj(win_pause_btn_menu)

# win_pause.run()

# игра
win_game = Game()
win_game.pause_run = win_pause.run


def play():
    win_game.new_maze(int(win_configurable_mode_spin_radius.text_))
    win_game.run()


def logining():
    if 0:
        return win_invalid_password.run
    return win_menu.run


# прикрепление функций к кнопкам


win_login.update_obj_fun('Play', logining())

win_invalid_password.update_obj_fun('Back', win_login.run)

win_menu.update_obj_fun('Play', win_configurable_mode.run)

win_configurable_mode.update_obj_fun('Hard mode', win_hard_mode.run)
win_configurable_mode.update_obj_fun('Menu', win_menu.run)

win_configurable_mode.update_obj_fun('Play', play)

win_hard_mode.update_obj_fun('Configurable mode', win_hard_mode.run)
win_hard_mode.update_obj_fun('Menu', win_menu.run)
win_hard_mode.update_obj_fun('Play', play)
# windows = [win_menu]
# def f():
#     global MENU_BACK
#     MENU_BACK = MENU_BACK_dict['Maze 3D']
#     for i in windows:
#         i.obj = MENU_BACK
#         i.back = MENU_BACK.run
win_pause.update_obj_fun('Menu', win_menu.run)
win_pause.update_obj_fun('Restart', play)
win_pause.update_obj_fun('Play', win_game.run)

win_login.run()
