import pygame as pg
import numpy as np
import taichi as ti
import taichi_glsl as ts
from taichi_glsl import vec2, vec3

ti.init(arch=ti.gpu)  # ti.cpu ti.gpu ti.vulkan ti.opengl ti.metal(macOS)
resolution = width, height = vec2(1200, 800)


# load texture


@ti.data_oriented
class PyShader:
    def __init__(self, app, texture):
        self.app = app
        self.screen_array = np.full((width, height, 3), [0, 0, 0], np.uint8)
        # taichi fields
        self.texture = pg.transform.rotate(pg.transform.scale(texture, (1024, 1024)),
                                           90)  # texture res - 2^n x 2^n (512 x 512, 1024 x 1024, ...)
        self.texture_size = self.texture.get_size()[0]
        # texture color normalization  0 - 255 --> 0.0 - 1.0
        texture_array = pg.surfarray.array3d(self.texture).astype(np.float32) / 255
        koef = 1
        self.screen_field = ti.Vector.field(3, ti.uint8, (width, height))
        self.texture_field = ti.Vector.field(3, ti.float32, self.texture.get_size())
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
            col += self.texture_field[st * self.texture_size]

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
