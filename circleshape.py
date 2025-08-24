import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def check_collide(self, obj) -> bool:
        distance = self.position.distance_to(obj.position)
        if distance <= self.radius + obj.radius:
            return True
        return False
    
    def check_in_bounds(self):
        x, y = self.position[0], self.position[1]
        if x < 0: # Check for Left Border
            pass