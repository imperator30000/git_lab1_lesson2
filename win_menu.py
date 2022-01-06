import pygame as pg


class Obj:
    def __init__(self, img, x_y,size, name):
        self.img = img
        self.x_y = x_y
        self.size = size
        self.name = name
        self.c = 0

class Window:
    def __init__(self, W_H):
        pg.init()
        self.sc = pg.display.set_mode(W_H)
        self.objs = []

    def render(self):
        [self.sc.blit(i.img, i.x_y) for i in self.objs]

    def check_obj(self, x, y):
        arr = []
        for i in self.objs:
            if i.x_y[0] <= x <= i.x_y[0] + i.size[0]




