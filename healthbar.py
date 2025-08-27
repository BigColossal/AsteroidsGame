import pygame

class Healthbar:
    # a healthbar that will be used for both asteroids and the player

    def __init__(self):
        self.height = 10

    def draw(self, entity, x, y, screen, width):
        surface = pygame.Surface((width, self.height))
        surface.fill((50, 50, 50))

        percent = (entity.health / entity.max_health)

        if percent > 0.5:
            color = (0, 255, 0)
        elif percent > 0.15:
            color = (255, 255, 0)
        else:
            color = (255, 0, 0)

        health_width = width * percent

        surface.fill(color, (0, 0, health_width, self.height))
        screen.blit(surface, (x, y))

        

