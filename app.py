from settings import pygame as pg
from settings import time
from settings import sys
from sceneGame import Game


class App:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((1920, 1080), pg.SCALED | pg.FULLSCREEN)
        self.clock = pg.time.Clock()
        self.running = True
        self.tps = 20
        self.skip_ticks = 1000 // self.tps
        self.max_frameskip = 10
        self.scene = Game(self.screen)

    def run(self):
        next_tick = time.time() * 1000
        while self.running:
            loops = 0
            while time.time() * 1000 > next_tick and loops < self.max_frameskip:
                self.handle_events()
                self.logic()
                self.get_stage()
                next_tick += self.skip_ticks
                loops += 1
            self.render()
        pg.quit()

    def render(self):
        self.scene.render()
        pg.display.flip()

    def logic(self):
        self.scene.logic()

    def handle_events(self):
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                sys.exit()
            elif ev.type == pg.KEYDOWN:
                if ev.key == pg.K_ESCAPE:
                    sys.exit()
        self.scene.handle_events()

    def get_stage(self):
        pass
