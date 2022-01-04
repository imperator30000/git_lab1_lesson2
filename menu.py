import pygame as pg
import numpy as np
import taichi as ti
import taichi_glsl as ts
from taichi_glsl import vec2, vec3

ti.init(arch=ti.cuda)  # ti.cpu ti.gpu ti.vulkan ti.opengl ti.metal(macOS)
resolution = width, height = vec2(1200, 800)

# load texture
texture = pg.transform.rotate(pg.transform.scale(pg.image.load('img/img.png'), (1024, 1024)), 90)  # texture res - 2^n x 2^n (512 x 512, 1024 x 1024, ...)
texture_size = texture.get_size()[0]
# texture color normalization  0 - 255 --> 0.0 - 1.0
texture_array = pg.surfarray.array3d(texture).astype(np.float32) / 255
koef = 1


@ti.data_oriented
class PyShader:
    def __init__(self, app):
        self.app = app
        self.screen_array = np.full((width, height, 3), [0, 0, 0], np.uint8)
        # taichi fields
        self.screen_field = ti.Vector.field(3, ti.uint8, (width, height))
        self.texture_field = ti.Vector.field(3, ti.float32, texture.get_size())
        self.texture_field.from_numpy(texture_array)

    @ti.kernel
    def render(self, time: ti.float32):
        """fragment shader imitation"""
        for frag_coord in ti.grouped(self.screen_field):
            # normalized pixel coords
            uv = (frag_coord - 0.5 * resolution) / resolution.y
            col = vec3(0.0)

            # polar coords
            phi = ts.atan(uv.y, uv.x)
            # rho = ts.length(uv)
            rho = pow(pow(uv.x ** 2, 10) + pow(uv.y ** 2, 100), 0.15)
            st = vec2(phi / ts.pi * 2, 0.25 / rho)
            st.x += 0
            st.y += time / 8
            col += self.texture_field[st * texture_size]

            col *= rho + 0.00001
            # col += 0.1 / rho * vec3(0.1, 0.1, 0.4)
            col = ts.clamp(col, 0.0, 1.0)
            self.screen_field[frag_coord.x, resolution.y - frag_coord.y] = col * 255

    def update(self):
        time = pg.time.get_ticks() * 0.001  # time in sec
        self.render(time)
        self.screen_array = self.screen_field.to_numpy()

    def draw(self):
        pg.surfarray.blit_array(self.app.screen, self.screen_array)

    def run(self):
        self.update()
        self.draw()


class App:
    def __init__(self):
        self.screen = pg.display.set_mode(resolution, pg.SCALED)
        self.clock = pg.time.Clock()
        self.shader = PyShader(self)

    def run(self):
        c = [0, 0, 0, 0]
        go_to_animation_zat_play = 1
        go_to_animation_zat_settings = 1
        go_to_animation_zat_title = 1
        go_to_animation_zat = 2
        next_win = 'play'
        while True:
            if go_to_animation_zat_title == 1:
                c[2] += 5
                if c[2] >= 255:
                    go_to_animation_zat_title = 0
                    c[2] = 255

            if go_to_animation_zat_play == 1:
                c[0] += 5
                if c[0] >= 255:
                    go_to_animation_zat_play = 0
                    c[0] = 255

            elif go_to_animation_zat_play == 3:
                c[0] -= 10
                if c[0] <= 150:
                    go_to_animation_zat_play = 0
                    c[0] = 150
            if go_to_animation_zat_settings == 1:
                c[1] += 5
                if c[1] >= 255:
                    go_to_animation_zat_settings = 0
                    c[1] = 255

            elif go_to_animation_zat_settings == 3:
                c[1] -= 10
                if c[1] <= 150:
                    go_to_animation_zat_settings = 0
                    c[1] = 150
            if go_to_animation_zat_settings == 2 and go_to_animation_zat_play == 2 and go_to_animation_zat_title == 2:
                minc = min(c[:-1])
                for i in range(3):
                    if c[i] != minc:
                        c[i] -= 5
                print(c)
                c3 = c[3]
                if c[0] == c[1] == c[2] >= 5:
                    c = [i - 5 for i in c[:-1]]
                    c.append(c3)
                else:
                    go_to_animation_zat = 1

                print(c)

            if go_to_animation_zat == 1:
                c[3] += 5
                if c[3] >= 255:
                    go_to_animation_zat = 0
                    c[3] = 255



            if go_to_animation_zat == 0:
                print(next_win)

            self.shader.run()
            # print(c, go_to_animation_zat_play, go_to_animation_zat_settings, go_to_animation_zat_title)
            imPlay = pg.transform.scale(pg.image.load('img/play.png'), (240, 160)).convert_alpha()
            imPlay.fill((255, 255, 255, c[0]), special_flags=pg.BLEND_RGBA_MULT)
            self.screen.blit(imPlay, (350, 400))

            imSettings = pg.transform.scale(pg.image.load('img/settings.png'), (240, 160)).convert_alpha()
            imSettings.fill((255, 255, 255, c[1]), special_flags=pg.BLEND_RGBA_MULT)
            self.screen.blit(imSettings, (610, 400))

            imTitle = pg.transform.scale(pg.image.load('img/title.png'), (500, 160)).convert_alpha()
            imTitle.fill((255, 255, 255, c[2]), special_flags=pg.BLEND_RGBA_MULT)
            self.screen.blit(imTitle, (350, 220))

            imBlack = pg.transform.scale(pg.image.load('img/black.png'), (1200, 800)).convert_alpha()
            imBlack.fill((255, 255, 255, c[3]), special_flags=pg.BLEND_RGBA_MULT)
            self.screen.blit(imBlack, (0, 0))
            pg.display.flip()
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    exit()
                if i.type == pg.MOUSEBUTTONDOWN:
                    if i.button == 3:
                        go_to_animation_zat_play = 1
                        go_to_animation_zat_settings = 1
                        go_to_animation_zat_title = 1
                        go_to_animation_zat = 2
                        c = [0,0,0,0]
                if (i.type == pg.MOUSEMOTION or i.type == pg.MOUSEBUTTONDOWN) and not go_to_animation_zat_play \
                        and not go_to_animation_zat_settings \
                        and not go_to_animation_zat_title:
                    if c[2]:
                        if 350 <= i.pos[0] <= 590 and 400 <= i.pos[1] <= 560:
                            if go_to_animation_zat_play == 0:
                                go_to_animation_zat_play = 3
                            if i.type == pg.MOUSEBUTTONDOWN and i.button == 1:
                                go_to_animation_zat_play = 2
                                go_to_animation_zat_settings = 2
                                go_to_animation_zat_title = 2
                                next_win = 'play'
                                print('play')
                        else:
                            go_to_animation_zat_play = 1

                        if 610 <= i.pos[0] <= 850 and 400 <= i.pos[1] <= 560:
                            if go_to_animation_zat_settings == 0:
                                go_to_animation_zat_settings = 3
                            if i.type == pg.MOUSEBUTTONDOWN and i.button == 1:
                                go_to_animation_zat_play = 2
                                go_to_animation_zat_settings = 2
                                go_to_animation_zat_title = 2
                                next_win = 'settings'
                                print('settings')

                        else:
                            if go_to_animation_zat_settings == 0:
                                go_to_animation_zat_settings = 1

            self.clock.tick(120)


if __name__ == '__main__':
    app = App()
    app.run()
