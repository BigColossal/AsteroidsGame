import pygame

class CoinCounter(pygame.sprite.Sprite):
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.score = 0
        self._color = (255, 255, 255)
        self.font = pygame.font.Font(None, 36)
        self.image = self.font.render(f"Score: {self.score}", True, self._color)
        self.rect = self.image.get_rect(topleft=(10, 10))

    def update(self, dt):
        self.image = self.font.render(f"Score: {self.score}", True, self._color)

    def add_value(self, coin):
        self.score += coin._value
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
