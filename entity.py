from gameObject import GameObject


class Entity(GameObject):
    def __init__(self, image, cords, world_cords):
        super().__init__(image, cords)
        self.world_cords = world_cords

    def move(self, moving):
        pass
