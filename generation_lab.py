import random
import sys
import pygame


class Road:
    def __init__(self, start, map_, num=2, back=True):
        self.num = num
        self.maps = map_

        self.back = back
        self.road = []
        # ↑0 →1 ↓2 ←3
        self.directions = [0, 1, 2, 3]
        self.directions = [1, 3, 2, 0]
        self.start = start
        self.points_ret = []

    def to_create(self):
        self.maps[self.start[1]][self.start[0]] = self.num
        data = [self.start[::1]]
        position = self.start[::1]
        self.road.append(tuple(position))
        run = True
        while run:

            positions = self.check_pos(position)

            try:
                position_old = position[::1]

                position = random.choice(positions)
                pos = [(position_old[_] + position[_]) // 2 for _ in range(2)]
                data.append(position)
                self.road.extend([tuple(pos), tuple(position)])
                self.maps[pos[1]][pos[0]] = self.num
                self.maps[position[1]][position[0]] = self.num
                n = self.check_pos(position_old)

                if n:
                    self.points_ret.append(tuple(position_old))


            except Exception:
                if self.back and self.points_ret:
                    while not self.check_pos(position):

                        if self.points_ret:
                            position = self.points_ret.pop()
                        else:
                            run = False
                            break

                else:
                    run = False
        # c = 10
        # for i in self.maps:
        #     print('\n', c, end='')
        #     for g in i:
        #         if g == self.num:
        #             print(0, end='')
        #         elif g == 9:
        #             print(' ', end='')
        #         else:
        #             print('_', end='')
        #     c += 1
        # for i in range(len(self.maps)):
        #     for g in range(len(self.maps[0])):
        #         if self.maps[i][g] == self.num:
        #             self.road.append([g, i])

    def check_pos(self, pos):
        positions = [[pos[0], pos[1] - 2],
                     [pos[0] + 2, pos[1]],
                     [pos[0], pos[1] + 2],
                     [pos[0] - 2, pos[1]]]
        ans = []
        for i in positions:
            try:
                if self.maps[i[1]][i[0]] not in (1, 9, self.num):
                    ans.append(i)
            except Exception:
                pass
        return ans

    def update(self):
        fun = lambda i, g: 1 if not i % 2 or i % 2 and not g % 2 else 0
        for i in range(len(self.maps)):
            for g in range(len(self.maps[0])):
                if self.maps[i][g] != 9:
                    self.maps[i][g] = fun(i, g)
        self.road = []
        self.points_ret = []
        self.to_create()


class Maze:
    def __init__(self, r):
        self.size = r * 2 + 1
        self.arr = [[]]
        self.maze_sekt = [[], [], [], []]
        self.r = r
        self.maze = [[]]
        self.k = 5
        self.l1 = 0
        self.l2 = 0
        self.l3 = 0
        self.maze_sekt_arr = [[], [], [], []]
        self.update_line()
        self.to_create()
        self.make_maze()

    def update_line(self, num=0):
        if not num or num == 1:
            self.l1 = random.randrange(self.r + 5, self.r + self.r * 2 ** 0.5 // 2 - 1, 2)
        if not num or num == 2:
            self.l2 = random.randrange(self.r + 5, self.r + self.r * 2 ** 0.5 // 2 - 1, 2)
        if not num or num == 3:
            self.l3 = random.randrange(self.r + 5, self.r + self.r * 2 ** 0.5 // 2 - 1, 2)

    def to_create(self):
        R = self.r
        fun = lambda i, g: 1 if not i % 2 or i % 2 and not g % 2 else 0
        arr = [[fun(i, g) for g in range(self.size)] for i in range(self.size)]

        X1 = R
        Y1 = R
        x = 0
        y = R
        delta = 1 - 2 * R
        num = 9
        arr1 = [[fun(i, g) for g in range(self.size)] for i in range(self.size)]
        arr2 = [[fun(i, g) for g in range(self.size)] for i in range(self.size)]
        arr3 = [[fun(i, g) for g in range(self.size)] for i in range(self.size)]
        arr4 = [[fun(i, g) for g in range(self.size)] for i in range(self.size)]
        c = 0
        while y >= x:
            arr1[Y1 - y][X1 + x] = num
            arr1[Y1 - y][X1 - x] = num

            arr2[Y1 + x][X1 + y] = num
            arr2[Y1 - x][X1 + y] = num

            arr3[Y1 + y][X1 + x] = num
            arr3[Y1 + y][X1 - x] = num

            arr4[Y1 + x][X1 - y] = num
            arr4[Y1 - x][X1 - y] = num
            if c and c <= R * 2 ** 0.5 // 2 + 1:
                k = c
                if c < self.k:
                    k = self.k
                arr1[R - k + 1][X1 + c] = num
                arr1[R - k + 1][X1 - c + 1] = num

                arr2[Y1 + c][R + k - 1] = num
                arr2[Y1 - c + 1][R + k - 1] = num

                arr3[R + k - 1][X1 + c - 1] = num
                arr3[R + k - 1][X1 - c] = num

                arr4[Y1 + c - 1][R - k + 1] = num
                arr4[Y1 - c][R - k + 1] = num

            error = 2 * (delta + y) - 1
            c += 1
            if (delta < 0) and (error <= 0):
                x += 1
                delta += 2 * x + 1
                continue
            if (delta > 0) and (error > 0):
                y -= 1
                delta -= 2 * y + 1
                continue
            x += 1
            y -= 1
            delta += 2 * (x - y)

        # c -= 1
        # arr = [[[[Y1 - y], [X1 + x]], [[R - c + 1], [X1 + c]]],
        #        [[[Y1 - y], [X1 - x]], [[R - c + 1], [X1 - c + 1]]],
        #        # [[[Y1 + x], [X1 + y]], [[Y1 - c + 1], [R + c - 1]]],
        #        # [[[Y1 - x], [X1 + y]], [[Y1 + c], [R + c - 1]]],
        #        [[[Y1 + y], [X1 + x]], [[R + c - 1], [X1 - c]]],
        #        [[[Y1 + y], [X1 - x]], [[R + c - 1], [X1 + c - 1]]],
        #        # [[[Y1 + x], [X1 - y]], [[Y1 - c], [R - c + 1]]],
        #        # [[[Y1 - x], [X1 - y]], [[Y1 + c - 1], [R - c + 1]]],
        #        ]
        # arr = [[(i[0][1][0] + i[1][1][0]) // 2, (i[0][0][0] + i[1][0][0]) // 2] for i in arr]
        # arr_ = [arr1, arr2, arr3, arr4]
        # print(arr)
        # for i in range(len(arr)):
        #     arr_[i // 2][arr[i][1]][arr[i][0]] = 9

        def fun1(arr):
            ans = []
            for i in range(len(arr)):
                try:
                    start_ = arr[i].index(9)
                    end_ = len(arr[i]) - arr[i][::-1].index(9)

                except ValueError:
                    start_ = len(arr[i]) - 1
                    end_ = 0

                for g in range(len(arr[i])):
                    if start_ >= g or g >= end_:
                        arr[i][g] = 9
                    elif arr[i][g] in (0, 1):
                        ans.append([g, i])
            return ans

        #
        # print(*arr, sep='\n', end='\n======================================================================\n')
        # print(*arr1, sep='\n', end='\n======================================================================\n')
        # print(*arr2, sep='\n', end='\n======================================================================\n')
        # print(*arr3, sep='\n', end='\n======================================================================\n')
        # print(*arr4, sep='\n', end='\n======================================================================\n')
        self.maze_sekt_arr = [fun1(arr1), fun1(arr2), fun1(arr3), fun1(arr4)]
        # print(self.maze_sekt_arr)

        # print(*arr, sep='\n', end='\n======================================================================\n')
        # print(*arr1, sep='\n', end='\n======================================================================\n')
        # print(*arr2, sep='\n', end='\n======================================================================\n')
        # print(*arr3, sep='\n', end='\n======================================================================\n')
        # print(*arr4, sep='\n', end='\n======================================================================\n')

        koor = [[R + 1, R - 1 - self.k], [R + 1 + self.k, R + 1], [R - 1, R + 1 + self.k], [R - 1 - self.k, R - 1]]
        roads = [arr1, arr2, arr3, arr4]
        for i in range(len(koor)):
            pos = [[koor[i][0] + 1, koor[i][1]],
                   [koor[i][0] - 1, koor[i][1]],
                   [koor[i][0], koor[i][1] + 1],
                   [koor[i][0], koor[i][1] - 1],
                   [koor[i][0] + 1, koor[i][1] - 1],
                   [koor[i][0] - 1, koor[i][1] + 1],
                   [koor[i][0] + 1, koor[i][1] + 1],
                   [koor[i][0] - 1, koor[i][1] - 1]]
            if roads[i][koor[i][1]][koor[i][0]]:

                for g in pos:

                    if not roads[i][g[1]][g[0]]:
                        koor[i] = g
                        break

        self.maze_sekt = [Road(koor[0], arr1),
                          Road(koor[1], arr2),
                          Road(koor[2], arr3),
                          Road(koor[3], arr4)]

        for i in self.maze_sekt:
            i.to_create()

        print(self.maze_sekt[0].road)
        if (self.r, self.r - 5) not in self.maze_sekt[0].road:
            self.maze_sekt[0].road.append((self.r, self.r - 5))
        if (1, self.r - 1) not in self.maze_sekt[3].road:
            self.maze_sekt[3].road.append((1, self.r - 1))
        # print(*arr, sep='\n', end='\n======================================================================\n')
        # print(*arr1, sep='\n', end='\n======================================================================\n')
        # print(*arr2, sep='\n', end='\n======================================================================\n')
        # print(*arr3, sep='\n', end='\n======================================================================\n')
        # print(*arr4, sep='\n', end='\n======================================================================\n')
        # print(ans)
        self.arr = arr

    def update_sek(self, num):

        self.maze_sekt[num].update()
        self.make_maze()

    def make_maze(self):
        def check_pos(arr, pos):
            return arr[pos[1]][pos[0]]

        arr = []
        for i in range(self.size):
            arr.append([])
            for g in range(self.size):
                pos = [check_pos(j.maps, (g, i)) for j in self.maze_sekt]
                if self.r - self.k + 2 <= g <= self.r + self.k - 2 and self.r - self.k + 2 <= i <= self.r + self.k - 2:
                    arr[i].append(0)
                elif 2 in pos or 0 in pos:
                    arr[i].append(0)
                elif 1 in pos:
                    arr[i].append(1)
                else:
                    arr[i].append(9)

        # print(*arr, sep='\n')
        self.maze = arr
        self.line()

    def line(self, update=True):
        self.maze[self.r - 1][0] = 0
        self.maze[self.r - 1][1] = 0
        self.maze[self.r - self.k][self.r] = 0
        self.maze[self.r - self.k + 1][self.r] = 0
        self.maze[-self.l1 - self.r % 2][self.l1 + self.r % 2] = 0
        self.maze[self.l2 + 1][self.l2] = 0
        self.maze[self.l3][-self.l3 - 2] = 0
        return len(self.maze) - self.l1 - self.r % 2, self.l1 + self.r % 2, self.l2 + 1, self.l2, self.l3, len(
            self.maze) - self.l3 - 2, [(self.l1 + self.r % 2, len(self.maze) - self.l1 - self.r % 2),
                                       (self.l2, self.l2 + 1), (len(self.maze) - self.l3 - 2, self.l3)]

    # [(0, self.r - 1), (1, self.r - 1), (self.r, self.r - self.k),
    #  (self.r, self.r - self.k + 1),
    #  (self.l1 + self.r % 2, len(self.maze) - self.l1 - self.r % 2),
    #  (self.l2, self.l2 + 1), (len(self.maze) - self.l3 - 2, self.l3)]

    def check_quat(self, x, y):
        if x == self.r and y in (self.r - self.k, self.r - self.k + 1):
            return 0
        for i in range(4):
            if (x, y) in self.maze_sekt[i].road:
                return i
        return 4



    def info(self):
        arr = self.line()
        # print(f'Проход между 1 и 2 сектором: x = {arr[1]} y = {arr[0]}')
        # print(f'Проход между 2 и 3 сектором: x = {arr[3]} y = {arr[2]}')
        # print(f'Проход между 3 и 4 сектором: x = {arr[5]} y = {arr[4]}')
        # print(f'вход: x = {self.r} y = {self.r} выход: x = {0} y = {self.r}')
        # print(*self.maze, sep='\n')
        # print(self.maze)
        # return (arr[1], arr[0]), (arr[3], arr[2]), (arr[5], arr[4]), (self.r, self.r), (0, self.r), self.maze
        return (self.r, self.r), self.maze, (0, self.r)





# ex2 = Maze(10)  # создание объекта лабиринта с каким-то радиусом
# ex2.make_maze()  # обновление лабиринта
# ex2.update_sek(1)  # обновление сектора (1, 2, 3, 4 - обновление сектора под номером )  1
# print(ex2.check_quat(9, 19))
#####################################################################################  4 2
#####################################################################################   3
# ex2.update_line()  # обновление координат проходов между секторами (0 - все, 1, 2, 3)    1
##################################################################################### 3  2

# ex2.info()  # выводит инфу
# # game = Game(500, ex2.maze)
# # keys = {'right': pygame.K_RIGHT,
# #         'left': pygame.K_LEFT,
# #         'up': pygame.K_UP,
# #         'down': pygame.K_DOWN}
# # keys1 = {'right': pygame.K_d,
# #          'left': pygame.K_a,
# #          'up': pygame.K_w,
# #          'down': pygame.K_s}
# #
# # game.add_players(Player(250, 250, 20, keys))
# # game.add_players(Player(250, 250, 10, keys1))
# #
# # while True:
# #     game.draw()
# #     game.events()
#
#
# def draw(screen, a, n):
#     b = a // n
#     screen.fill((0, 0, 0))
#     for i in range(n):
#         for g in range(n):
#             try:
#                 if ex2.maze[i][g] == 0:
#                     pygame.draw.rect(screen, (255, 255, 255), (g * b, i * b, b, b))
#             except Exception:
#                 continue
#
#
# C = 9
# if __name__ == '__main__':
#     # инициализация Pygame:
#     pygame.init()
#     # размеры окна:
#
#     # screen — холст, на котором нужно рисовать:
#     screen = pygame.display.set_mode((500, 500))
#     # формирование кадра:
#     # команды рисования на холсте
#
#     # ...
#     # ...
#     # смена (отрисовка) кадра:
#     draw(screen, 500, 220)
#
#     pygame.display.flip()
#     pygame.display.set_caption('Крест')
#     clock = pygame.time.Clock()
#
#     # ожидание закрытия окна:
#     while pygame.event.wait().type != pygame.QUIT:
#         pass
#     # завершение работы:
#     run = True
#     while run:
#         print(C)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#
#         # ex2.update_sek(C % 4)
#         # ex2.make_maze()
#         ex2 = Maze(C + 11)
#         # print(ex2.maze)
#         # ex2.to_create()
#         # ex2.make_maze()
#         # ex2 = Maze(15)
#         # ex2.to_create()
#         # ex2.make_maze()
#         # ex2.update_line(0)
#         # ex2.line()
#         draw(screen, 1000, 200)
#
#         # clock.tick(1)
#
#         pygame.display.flip()
#         # screen.fill((0, 0, 0))
#         C += 1
#     pygame.quit()
#
# # print(ex.road)
# # ex1 = Road('right', 8, maps, 3)
# # ex1.to_create()
# #
# # ex2 = Road('down', 2, maps, 4, True)
# # ex2.to_create()
# # ex2 * ex1
# # ex2 * ex
# # for i in ex1.road:
# #     print('\n')
# #     for g in i:
# #         if g in (2, 3, 4):
# #             print(0, end='')
# #
# #         elif g == 9:
# #             print(' ', end='')
# #         else:
# #             print('_', end='')
