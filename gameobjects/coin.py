import pygame

class Coin(pygame.sprite.Sprite):
    def __init__(self, position):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self._value = 1
        self._position = position
        self._color = (255, 255, 0)
        self._radius = 10

    def draw(self, screen):
        pygame.draw.circle(screen, self._color, (self._position[0], self._position[1]), self._radius)

    def collides_with(self, other):
        return self.position.distance_to(other.position) <= self._radius + other.radius