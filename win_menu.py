import pygame as pg
from settings import *
from generation_lab import *


class Obj:
    def __init__(self, img, x_y, size, name, text='', font_size=70, c=255, e=255, ch=False, ok=255,
                 min_max=(11, 99), fun=lambda: '', step_spin=1, go_next_win=True):
        self.curs = 0
        self.active = False
        self.rect = pg.Rect(*x_y, *size)
        self.img = pg.transform.scale(img, size).convert_alpha()
        self.x_y = x_y
        self.size = size
        self.name = name
        self.changing = ch
        self.step = 5
        self.end_counter = e
        self.counter = c
        self.koef = 1
        self.ok_end = ok
        self.dependent_objects = []
        self.fun = fun
        self.enabled = False
        self.font_size = font_size
        self.font = pg.font.SysFont('', font_size)
        self.text = self.font.render(text, True, (20, 20, 20)).convert_alpha()
        text_size = self.text.get_size()
        self.text_x_y = [self.x_y[i] + (self.size[i] - text_size[i]) // 2 for i in range(2)]
        self.text_ = text
        self.min_max = min_max
        self.nex_win = False
        self.step_spin = step_spin
        self.go_next_win = go_next_win
        self.recover()

    def spin(self, x_y, k):
        pass

    def update_text(self):
        self.text = self.font.render(self.text_, True, (0, 0, 0)).convert_alpha()
        self.text_x_y = [self.x_y[i] + (self.size[i] - self.text.get_size()[i]) // 2 for i in range(2)]
        self.text.set_alpha(self.counter)

    def in_obj(self, x_y):
        a = [self.x_y[g] <= x_y[g] <= self.x_y[g] + self.size[g] for g in range(2)]
        return all(a)

    def recover(self, pressed=False):
        self.go_animation(self.ok_end, 5)

        for i in self.dependent_objects:
            if not i.changing and (not i.enabled or pressed):
                i.go_animation(self.ok_end, 5)
            if pressed:
                i.enabled = False

        self.enabled = False

    def choice(self, x_y):

        if not self.enabled:
            a = self.in_obj(x_y)
            if a:
                self.go_animation(150, 5)
                for i in self.dependent_objects:
                    if not i.enabled:
                        i.go_animation(150, 5)
            else:
                self.recover()

    def pressed(self, x_y):
        pass

    def go_animation(self, end, step):

        self.changing = True
        self.step = step
        self.end_counter = end
        if self.counter < self.end_counter:
            self.koef = 1
        else:
            self.koef = -1

    def animation(self, obj):
        if self.changing:
            self.counter += self.koef * self.step
            if self.counter * self.koef >= self.end_counter * self.koef:
                self.counter = self.end_counter
                self.changing = False
                if self.enabled:
                    self.recover(True)
                    if self.go_next_win:
                        obj.screen.fill((0, 0, 0))
                    self.fun()

            self.text.set_alpha(self.counter)
            self.img.set_alpha(self.counter)

    def input_txt(self, sim):
        pass


class Title(Obj):
    def choice(self, x_y):
        pass


class SpinBox(Obj):
    def spin(self, x_y, k):
        text_ = int(self.text_)
        a = self.in_obj(x_y)
        if self.min_max[0] <= text_ + self.step_spin * k <= self.min_max[1] and a:
            self.text_ = str(text_ + self.step_spin * k)
            self.update_text()
            self.fun()
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE] and self.min_max[0] <= text_ + 10 * k <= self.min_max[1] and a:
            self.text_ = str(text_ + 10 * k)
            self.update_text()
            self.fun()


class Button(Obj):

    def pressed(self, x_y):
        a = self.in_obj(x_y)
        if a:
            if not self.enabled:
                self.enabled = True
                self.go_animation(0, 5)
                for i in self.dependent_objects:
                    i.enabled = True
                    i.go_animation(0, 5)
                return True
            else:

                self.recover(True)
        return False


class InputBox(Obj):

    def input_txt(self, sim):

        self.curs += 1
        if self.active:
            if sim != 'backspace':
                self.text_ += sim
            elif sim == 'backspace':
                self.text_ = self.text_[:-1]

            self.text = self.font.render(self.text_, True, (0, 0, 0)).convert_alpha()
            if self.text.get_size()[0] > self.size[0] - self.font_size // 2:
                self.text_ = self.text_[:-1]
            self.text = self.font.render(self.text_, True, (0, 0, 0)).convert_alpha()
            self.text_x_y = [self.x_y[i] + (self.size[i] - self.text.get_size()[i]) // 2 for i in range(2)]

    def choice(self, x_y):
        self.active = False
        self.recover()
        if self.in_obj(x_y):
            self.go_animation(150, 5)
            self.active = True
        else:
            self.text = self.font.render(self.text_, True, (0, 0, 0)).convert_alpha()
            self.text_x_y = [self.x_y[i] + (self.size[i] - self.text.get_size()[i]) // 2 for i in range(2)]

    def recover(self, pressed=False):
        self.go_animation(self.ok_end, 5)
        for i in self.dependent_objects:
            if not i.changing:
                i.go_animation(self.ok_end, 5)


class Back:
    def __init__(self, obj):
        self.obj = obj
        self.img = pg.transform.scale(pg.image.load(obj.name_f), obj.size)

    def iteration(self):
        pass

    def run(self):
        self.img.blit(self.obj.screen, (0, 0))
        self.iteration()


class Window:
    def __init__(self, W_H, obj=None):

        pg.init()
        pg.font.init()
        self.screen = pg.display.set_mode(W_H)
        self.objs = dict()
        self.size = W_H
        self.returned = dict()
        self.black = Title(pg.image.load('img/black.png'), (0, 0), W_H, 'black', ch=True, ok=0, e=0, c=255)
        self.clock = pg.time.Clock()
        self.m_action = [False, False, False, False]  # движение нажатие
        self.m_pos = (-1, -2)
        self.name_f = 'img/black.png'
        try:
            self.obj = obj(self)
        except TypeError:
            if not obj is None:
                self.name_f = obj
            self.obj = Back(self)

    def update_back(self, back):
        self.obj = back(self)

    def update_obj_fun(self, name, fun):
        for i in self.objs:
            if self.objs[i].name == name:
                self.objs[i].fun = fun
                break

    def render(self):
        a = [[self.screen.blit(self.objs[i].img, self.objs[i].x_y),
              self.screen.blit(self.objs[i].text, self.objs[i].text_x_y)] for i in self.objs]

    def add_obj(self, obj, dependent_objects_name=()):
        if obj.name in self.objs:
            return False
        self.objs[obj.name] = obj
        dependent_objects = []
        for i in dependent_objects_name:
            dependent_objects.append(self.objs[i])
        obj.dependent_objects = dependent_objects

    def restart(self):
        for i in self.objs:
            self.objs[i].enabled = False
            if self.objs[i].name != 'black':
                self.objs[i].counter = 0

            self.objs[i].go_animation(self.objs[i].ok_end, 5)

    def run(self):
        pg.display.flip()
        pg.mouse.set_visible(True)
        self.black = Title(pg.image.load('img/black.png'), (0, 0), self.size, 'black', ch=True, ok=0, e=0, c=255)
        self.objs['black'] = self.black
        self.restart()
        while True:
            sim = ''
            self.obj.run()
            self.m_action = [False, False, False, False]
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    exit()
                if i.type == pg.KEYDOWN:
                    if i.key == pg.K_BACKSPACE:
                        sim = 'backspace'
                    else:
                        sim = i.unicode

                if i.type == pg.MOUSEBUTTONDOWN:
                    if i.button == 1:
                        self.m_action[1] = True

                    if i.button == 4:
                        self.m_action[2] = True

                    if i.button == 5:
                        self.m_action[3] = True

                    self.m_pos = i.pos

                if i.type == pg.MOUSEMOTION:
                    self.m_action[0] = True
                    self.m_pos = i.pos

            for i in self.objs:
                self.objs[i].animation(self)
                self.objs[i].input_txt(sim)
                if any(self.m_action[:2]):
                    self.objs[i].choice(self.m_pos)
                if self.m_action[1]:
                    pressed = self.objs[i].pressed(self.m_pos)
                    if pressed and self.objs[i].go_next_win:
                        self.black.ok_end = 255

                if self.m_action[2]:
                    self.objs[i].spin(self.m_pos, 1)
                if self.m_action[3]:
                    self.objs[i].spin(self.m_pos, -1)

                self.returned[self.objs[i].name] = self.objs[i].text_

                # print(self.m_action)

            self.render()

            pg.display.flip()
            self.clock.tick(60)


class MazeB(Back):
    counter = 0
    maze = None
    step = 5
    size = 20

    def update(self):
        self.counter = 0
        fun = lambda x, y: 1 if y % 2 or x % 2 else 0
        arr = [[fun(g, i) for g in range((self.obj.size[0] - 60) // self.size)] for i in
               range((self.obj.size[1] - 60) // self.size)]

        m_pos = [(i - 10) // self.size - 1 for i in self.obj.m_pos]
        if fun(*m_pos):
            start = [i - 1 for i in m_pos]
            pos = []
            for i in range(3):
                for g in range(3):
                    pos.append([start[0] + g, start[1] + i])
            for g in pos:
                if not fun(*g) and 0 <= g[0] <= (self.obj.size[0] - 60) // self.size and 0 <= g[1] <= (
                        self.obj.size[1] - 60) // self.size:
                    m_pos = g
                    break

        if not fun(*m_pos) and 0 <= m_pos[0] <= (self.obj.size[0] - 60) // self.size and 0 <= m_pos[1] <= (
                self.obj.size[1] - 60) // self.size:
            self.maze = Road(m_pos, arr)
            self.maze.to_create()

        else:
            self.maze = Road([0, 0], arr)
            self.maze.to_create()

    def back(self):
        if self.maze is None:
            self.update()
        if self.counter + self.step >= len(self.maze.road):
            self.step *= -1

        elif self.counter + self.step <= 0:
            self.step *= -1
            self.update()

        self.counter += self.step
        for i in range(self.counter):
            try:
                pg.draw.rect(self.obj.screen, (25, 25, 25),
                             (30 + self.maze.road[i][0] * self.size,
                              30 + self.maze.road[i][1] * self.size, self.size, self.size))
            except Exception:
                self.obj.m_pos = [30, 30]
                self.update()
                break

    def iteration(self):
        self.obj.screen.fill((150, 150, 150))
        pg.draw.rect(self.obj.screen, (75, 75, 75),
                     (10, 10, self.obj.size[0] - 20, self.obj.size[1] - 20))
        self.back()


#
#
# window = Window((1200, 800), MazeB)
# window1 = Window((1200, 800), MazeB)
# window.run()

# app = Window((1200, 800), pg.image.load('img/back.png'))
# app.run()
