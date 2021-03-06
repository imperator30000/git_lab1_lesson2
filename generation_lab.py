import random


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

        self.maze_sekt_arr = [fun1(arr1), fun1(arr2), fun1(arr3), fun1(arr4)]

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

        if (self.r, self.r - 5) not in self.maze_sekt[0].road:
            self.maze_sekt[0].road.append((self.r, self.r - 5))
        if (1, self.r - 1) not in self.maze_sekt[3].road:
            self.maze_sekt[3].road.append((1, self.r - 1))

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

    def check_quat(self, x=0, y=0, fl=False, walls=False):
        if fl and x == self.r and y in (self.r - self.k, self.r - self.k + 1):
            return 0
        for i in range(4):
            if (x, y) in self.maze_sekt[i].road:
                return i
            if self.maze_sekt[i].maps[y][x] in (1, 2):
                if walls:
                    return i
                return 4
        return 4

    def in_walls(self, x, y):
        if self.maze[int(y)][int(x)]:
            return True

        return False

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
