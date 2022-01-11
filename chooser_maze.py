import pygame as pg

resolution = width, height = 1200, 800


class App:
    def __init__(self):
        self.screen = pg.display.set_mode(resolution, pg.SCALED)
        self.clock = pg.time.Clock()

    def anim(self, counter, koef, end, step=5):
        counter = koef * step + counter
        if counter * koef >= end * koef:
            counter = end
            return counter, True
        return counter, False

    def run(self):
        c = [255]
        anim_bool = [0]
        while True:
            c[0], ending = self.anim(c[0], -1, 0, 10)
            im = pg.transform.scale(pg.image.load('img/img.png'), (1200, 800)).convert_alpha()
            imBlack = pg.transform.scale(pg.image.load('img/black.png'), (1200, 800)).convert_alpha()
            imBlack.fill((255, 255, 255, c[0]), special_flags=pg.BLEND_RGBA_MULT)
            self.screen.blit(im, (0, 0))
            self.screen.blit(imBlack, (0, 0))

            pg.display.flip()
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    exit()
            self.clock.tick(120)


if __name__ == '__main__':
    app = App()
    app.run()
