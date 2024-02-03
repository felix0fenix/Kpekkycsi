from classWorld import World


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.world = World()

    def render(self):
        self.screen.fill((30, 30, 30))
        self.world.render()

    def handle_events(self):
        self.world.handle_events()

    def logic(self):
        self.world.logic()
