from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius, kind, color=None):
        super().__init__(x, y, radius)
        self.kind = kind
        self.damage = 1
        self.max_health = self.get_health()
        self.health = self.max_health
        self.hit = False
        self.hit_visual_cd = 0.3
        self.hit_visual_timer = 0
        if color:
            self.og_color = color
        else:
            self.og_color = self.select_random_color()
        self.color = self.og_color

    def select_random_color(self):
        import random
        color_selection = [#(255, 200, 200), # Red
                           #(255, 200, 100), # Orange
                           (255, 255, 200), # yellow
                           #(200, 255, 200), # Green
                           #(180, 220, 255), # Blue
                           #(200, 175, 255), # Violet
                           ]
        
        return random.choice(color_selection)
        

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
            angle = 45
            vector1, vector2 = self.velocity.rotate(angle), self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            offset_distance = new_radius * 1.5
            
            pos1 = self.position + vector1.normalize() * offset_distance
            pos2 = self.position + vector2.normalize() * offset_distance

            asteroid1 = Asteroid(pos1.x, pos1.y, new_radius, self.kind - 1, self.og_color)
            asteroid2 = Asteroid(pos2.x, pos2.y, new_radius, self.kind - 1, self.og_color)

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