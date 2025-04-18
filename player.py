from circleshape import CircleShape
from constants import *
import pygame
from shot import Shot

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.__rotation = 0
        self.cooldown = 0


    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.__rotation)
        right = pygame.Vector2(0, 1).rotate(self.__rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.__rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.cooldown -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        self.position += pygame.Vector2(0, 1).rotate(self.__rotation) * PLAYER_SPEED * dt

    def shoot(self):
        if not self.cooldown > 0:
            bullet = Shot(self.position[0], self.position[1], SHOT_RADIUS)
            forward = pygame.Vector2(0, 1).rotate(self.__rotation) * PLAYER_SHOOT_SPEED
            bullet.velocity = forward
            self.cooldown = PLAYER_SHOOT_COOLDOWN