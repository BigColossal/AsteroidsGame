import pygame

class coinCounter(pygame.sprite.Sprite):
    def __init__(self):
        from constants import FONT as font
        super().__init__()
        self.score = 0
        self._color = (255, 255, 255)
        self.image = font.render(f"Score: {self.score}", True, self._color)
        self.rect = self.image.get_rect(topleft=(10, 10))

    def update(self, dt):
        pass
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
