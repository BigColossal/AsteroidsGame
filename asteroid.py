from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(25, 50)
        vector_a, vector_b = self.velocity.rotate(random_angle), self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_a, new_asteroid_b = Asteroid(self.position[0], self.position[1], new_radius), Asteroid(self.position[0], self.position[1], new_radius)
        new_asteroid_a.velocity, new_asteroid_b.velocity = vector_a * 1.2, vector_b * 1.2
