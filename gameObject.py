from settings import pygame as pg


class GameObject:
    def __init__(self, image, screen_cords):
        self.image = pg.transform.scale(
            image, (image.get_width() * 10,
                    image.get_height() * 10)
        )
        self.rect = self.image.get_rect()
        self.screen_cords = screen_cords
        self.rect.topleft = self.screen_cords

    def render(self, screen):
        screen.blit(self.image, self.screen_cords)

    def change_screen_cords(self, cords):
        self.screen_cords = (self.screen_cords[0] + cords[0], self.screen_cords[1] + cords[1])
        
