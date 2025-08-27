from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius, kind):
        super().__init__(x, y, radius)
        self.kind = kind
        self.damage = 1
        self.max_health = self.get_health()
        self.health = self.max_health
        self.hit = False
        self.hit_visual_cd = 0.3
        self.hit_visual_timer = 0
        self.og_color = (255, 255, 255)
        self.color = self.og_color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
        if self.hit:
            self.hit_visual_timer -= dt
            if self.hit_visual_timer <= 0:
                self.hit = False
                self.color = self.og_color

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            vector1, vector2 = self.velocity.rotate(angle), self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            x, y = self.position[0], self.position[1]
            asteroid1, asteroid2 = Asteroid(x, y, new_radius, self.kind - 1), Asteroid(x, y, new_radius, self.kind - 1)
            asteroid1.velocity = vector1 * 1.2
            asteroid2.velocity  = vector2 * 1.2       

    def get_health(self):
        if self.kind == 1:
            return 1
        else:
            return 2 * (self.kind - 1)
        
    def get_hit(self, damage):
        self.hit = True
        self.hit_visual_timer = self.hit_visual_cd
        self.color = (255, 0, 0)

        self.health -= damage
        if self.health <= 0:
            self.split()
