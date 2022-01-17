import pygame as pg
from generation_lab import Road


class MazeBack:
    def __init__(self, obj, texture):
        self.obj = obj
        self.counter = 0
        self.maze = None
        self.step = 5
        self.size = 20
        self.update()

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

        if self.counter + self.step >= len(self.maze.road):
            print('popp')
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

    def run(self):
        self.obj.screen.fill((150, 150, 150))
        pg.draw.rect(self.obj.screen, (75, 75, 75),
                     (10, 10, self.obj.size[0] - 20, self.obj.size[1] - 20))
        self.back()
