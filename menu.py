from win_menu import *
import pygame as pg
from main import Game

BACK_MUZ.play(-1)
# регистрация/вход
win_login = Window((1200, 800), MENU_BACK)
win_login_input_login = InputBox(pg.image.load('img/brick_.png'), (80, 480), (500, 80), 'Login_input', 'btn',
                                 font_size=30)
win_login_input_password = InputBox(pg.image.load('img/brick_.png'), (620, 480), (500, 80), 'Password_input', 'btn',
                                    font_size=30)
win_login_title_maze = Obj(pg.image.load('img/brick_.png'), (310, 80), (590, 200), 'Maze', 'title', 'Maze', 100)
win_login_title_password = Obj(pg.image.load('img/brick_.png'), (620, 360), (500, 80), 'Password', 'title', 'Password')
win_login_title_login = Obj(pg.image.load('img/brick_.png'), (80, 360), (500, 80), 'Login', 'title', 'Login')
win_login_btn_play = Obj(pg.image.load('img/brick_.png'), (450, 640), (300, 80), 'Play', 'btn', 'Play')

win_login.add_obj(win_login_title_maze)
win_login.add_obj(win_login_title_password)
win_login.add_obj(win_login_title_login)
win_login.add_obj(win_login_btn_play)
win_login.add_obj(win_login_input_login)
win_login.add_obj(win_login_input_password)

# неверный пароль
win_invalid_password = Window((1200, 800), MENU_BACK)

win_invalid_password_title = Obj(pg.image.load('img/brick_.png'), (100, 80), (1000, 100), 'Invalid password', 'title',
                                 'An invalid password or an account with such a login exists', font_size=40)
win_invalid_password_btn_menu = Obj(pg.image.load('img/brick_.png'), (450, 640), (300, 80), 'Back', 'btn', 'Back')

win_invalid_password.add_obj(win_invalid_password_title)
win_invalid_password.add_obj(win_invalid_password_btn_menu)

# меню
win_menu = Window((1200, 800), MENU_BACK)

win_menu_btn_play = Obj(pg.image.load('img/brick_.png'), (310, 450), (270, 100), 'Play', 'btn', 'Play')
win_menu_btn_settings = Obj(pg.image.load('img/brick_.png'), (630, 450), (270, 100), 'Settings', 'btn', 'Settings', 60)
win_menu_title_title = Obj(pg.image.load('img/brick_.png'), (310, 210), (590, 200), 'Maze', 'title', 'Maze', 100)

win_menu.add_obj(win_menu_btn_play)
win_menu.add_obj(win_menu_btn_settings)
win_menu.add_obj(win_menu_title_title)

# настройки

win_settings = Window((1200, 800), MENU_BACK)

win_settings_btn_sound = Obj(pg.image.load('img/brick_.png'), (200, 150), (350, 100), 'Sound', 'btn', 'Sound')
win_settings_btn_account = Obj(pg.image.load('img/brick_.png'), (200, 350), (350, 100), 'Account', 'btn', 'Account')
win_settings_btn_menu_textures = Obj(pg.image.load('img/brick_.png'), (650, 350), (350, 100), 'Menu textures', 'btn',
                                     'Menu textures')
win_settings_btn_textures = Obj(pg.image.load('img/brick_.png'), (650, 150), (350, 100), 'Textures', 'btn', 'Textures')
win_settings_btn_back = Obj(pg.image.load('img/brick_.png'), (200, 550), (800, 100), 'Back', 'btn', 'Back')

win_settings.add_obj(win_settings_btn_sound)
win_settings.add_obj(win_settings_btn_account)
win_settings.add_obj(win_settings_btn_textures)
win_settings.add_obj(win_settings_btn_menu_textures)
win_settings.add_obj(win_settings_btn_back)
# win_settings.add_obj(win_configurable_mode_spin_radius)
# win_settings.run()


# звук

win_sound = Window((1200, 800), MENU_BACK)
win_sound_title_music = Obj(pg.image.load('img/brick_.png'), (50, 200), (300, 100), 'Music', 'title', 'Music')
win_sound_spin_music = Obj(pg.image.load('img/brick_.png'), (950, 200), (100, 100), 'Spin music', 'spin', '50',
                           min_max=[0, 50])

win_sound_title_menu = Obj(pg.image.load('img/brick_.png'), (50, 350), (300, 100), 'Menu', 'title', 'Menu')
win_sound_spin_menu = Obj(pg.image.load('img/brick_.png'), (950, 350), (100, 100), 'Spin menu', 'spin', '50',
                          min_max=[0, 50])

win_sound_title_game = Obj(pg.image.load('img/brick_.png'), (50, 500), (300, 100), 'Game', 'title', 'Game')
win_sound_spin_game = Obj(pg.image.load('img/brick_.png'), (950, 500), (100, 100), 'Spin game', 'spin', '50',
                          min_max=[0, 50])
win_sound_title_all = Obj(pg.image.load('img/brick_.png'), (50, 50), (300, 100), 'All', 'title', 'All')
win_sound_spin_all = Obj(pg.image.load('img/brick_.png'), (950, 50), (100, 100), 'Spin all', 'spin', '50',
                         min_max=[0, 50])

win_sound_btn_back = Obj(pg.image.load('img/brick_.png'), (50, 650), (300, 100), 'Back', 'btn', 'Back')

win_sound.add_obj(win_sound_title_music)
win_sound.add_obj(win_sound_spin_music, ['Music'])
win_sound.add_obj(win_sound_title_menu)
win_sound.add_obj(win_sound_spin_menu, ['Menu'])
win_sound.add_obj(win_sound_title_game)
win_sound.add_obj(win_sound_spin_game, ['Game'])
win_sound.add_obj(win_sound_title_all)
win_sound.add_obj(win_sound_spin_all, ['Spin music', 'Spin menu', 'Spin game', 'All', 'Music', 'Menu', 'Game'])
win_sound.add_obj(win_sound_btn_back)

# win_sound.run()
# аккаунт

win_account = Window((1200, 800), MENU_BACK)

win_account_btn_account = Obj(pg.image.load('img/brick_.png'), (300, 200), (600, 150), 'Account', 'btn',
                              'login or registration')
win_account_btn_back = Obj(pg.image.load('img/brick_.png'), (300, 450), (600, 150), 'Back', 'btn', 'Back')

win_account.add_obj(win_account_btn_account)
win_account.add_obj(win_account_btn_back)

# win_account.run()
# текстуры

win_textures = Window((1200, 800), MENU_BACK)

win_textures_btn_Red_brick = Obj(TEXTURES['Red brick'], (350, 200), (200, 200), 'Red brick', 'btn',
                                 'Red brick', 40, go_next_win=False)

win_textures_btn_Grey_brick = Obj(TEXTURES['Grey brick'], (650, 200), (200, 200), 'Grey brick', 'btn',
                                  'Grey brick', 40, go_next_win=False)
win_textures_btn_back = Obj(pg.image.load('img/brick_.png'), (350, 450), (500, 150), 'Back', 'btn', 'Back')

win_textures.add_obj(win_textures_btn_Red_brick)
win_textures.add_obj(win_textures_btn_Grey_brick)
win_textures.add_obj(win_textures_btn_back)

# текстуры меню

win_menu_textures = Window((1200, 800), MENU_BACK)

win_menu_textures_btn_maze_2d = Obj(pg.image.load('img/brick_.png'), (300, 200), (250, 150), 'Maze 2D', 'btn',
                                    'Maze 2D', go_next_win=False)

win_menu_textures_btn_maze_3d = Obj(pg.image.load('img/brick_.png'), (650, 200), (250, 150), 'Maze 3D', 'btn',
                                    'Maze 3D', go_next_win=False)
win_menu_textures_btn_back = Obj(pg.image.load('img/brick_.png'), (300, 450), (600, 150), 'Back', 'btn', 'Back')

win_menu_textures.add_obj(win_menu_textures_btn_maze_2d)
win_menu_textures.add_obj(win_menu_textures_btn_maze_3d)
win_menu_textures.add_obj(win_menu_textures_btn_back)

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
    # fl = logining_(win_login_input_login.text_, win_login_input_password.text_)
    if True or not win_login_input_login.text_ or not win_login_input_password.text_:
        return win_invalid_password.run()
    return win_menu.run()


def volume_menu(num=None):
    if num is None:
        VOLUME[1] = int(win_sound_spin_menu.text_) / 50
    else:
        VOLUME[1] = num[0]
        win_sound_spin_menu.text_ = num[1]
        win_sound_spin_menu.update_text()
    CLICK_SOUND.set_volume(VOLUME[1])


def volume_music(num=None):
    if num is None:
        VOLUME[0] = int(win_sound_spin_music.text_) / 50
    else:
        VOLUME[0] = num[0]
        win_sound_spin_music.text_ = num[1]
        win_sound_spin_music.update_text()
    BACK_MUZ.set_volume(VOLUME[0])


def volume_game(num=None):
    if num is None:
        VOLUME[2] = int(win_sound_spin_game.text_) / 50
    else:
        VOLUME[2] = num[0]
        win_sound_spin_game.text_ = num[1]
        win_sound_spin_game.update_text()
    BACK_MUZ.set_volume(VOLUME[2])


def volume_all():
    num = [int(win_sound_spin_all.text_) / 50, win_sound_spin_all.text_]
    volume_music(num)
    volume_menu(num)
    volume_game(num)


def update_all_win():
    back = MENU_BACK
    win_login.update_back(back)
    win_menu.update_back(back)
    win_invalid_password.update_back(back)
    win_hard_mode.update_back(back)
    win_configurable_mode.update_back(back)
    win_pause.update_back(back)
    win_settings.update_back(back)
    win_sound.update_back(back)
    win_account.update_back(back)
    win_menu_textures.update_back(back)
    win_textures.update_back(back)


def update_all_win_3D():
    # SELECTED_TEXTURES[0] = TEXTURES['Red brick']
    global MENU_BACK
    MENU_BACK = PyShader
    update_all_win()


def update_all_win_2D():
    # SELECTED_TEXTURES[0] = TEXTURES['Red brick']
    global MENU_BACK
    MENU_BACK = MazeBack
    update_all_win()


def update_textures_Red_brick():
    SELECTED_TEXTURES[0] = TEXTURES['Red brick']
    update_all_win()


def update_textures_Grey_brick():
    SELECTED_TEXTURES[0] = TEXTURES['Grey brick']
    update_all_win()


# прикрепление функций к кнопкам


win_login.update_obj_fun('Play', logining)

win_invalid_password.update_obj_fun('Back', win_login.run)

win_menu.update_obj_fun('Play', win_configurable_mode.run)
win_menu.update_obj_fun('Settings', win_settings.run)

win_configurable_mode.update_obj_fun('Hard mode', win_hard_mode.run)
win_configurable_mode.update_obj_fun('Menu', win_menu.run)

win_configurable_mode.update_obj_fun('Play', play)

win_hard_mode.update_obj_fun('Configurable mode', win_configurable_mode.run)
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

win_settings.update_obj_fun('Sound', win_sound.run)
win_settings.update_obj_fun('Back', win_menu.run)
win_settings.update_obj_fun('Account', win_account.run)
win_settings.update_obj_fun('Menu textures', win_menu_textures.run)
win_settings.update_obj_fun('Textures', win_textures.run)

win_sound.update_obj_fun('Spin music', volume_music)
win_sound.update_obj_fun('Spin menu', volume_menu)
win_sound.update_obj_fun('Spin game', volume_game)
win_sound.update_obj_fun('Spin all', volume_all)
win_sound.update_obj_fun('Back', win_settings.run)

win_account.update_obj_fun('Account', win_login.run)
win_account.update_obj_fun('Back', win_settings.run)

win_menu_textures.update_obj_fun('Back', win_settings.run)
win_menu_textures.update_obj_fun('Maze 2D', update_all_win_2D)
win_menu_textures.update_obj_fun('Maze 3D', update_all_win_3D)

win_textures.update_obj_fun('Red brick', update_textures_Red_brick)
win_textures.update_obj_fun('Grey brick', update_textures_Grey_brick)
win_textures.update_obj_fun('Back', win_settings.run)



# update_all_win()
win_login.run()
