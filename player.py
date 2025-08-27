from circleshape import CircleShape
from constants import *
import pygame
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cd = 0.3
        self.max_health = 10
        self.health = self.max_health
        self.shoot_cd_timer = 0
        self.damage = 1

        self.invincible_period_time = 0.5
        self.invincible_timer = 0
        self.invincible = False

        self.color = (255, 255, 255)
        self.knockback = 100

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def get_hit(self, damage: float):
        if not self.invincible:
            self.health -= damage
            self.handle_invincible(switch=True)

    def handle_invincible(self, switch):
        if switch == False:
            self.invincible = False
            self.color = (255, 255, 255)
        else:
            self.invincible = True
            self.invincible_timer = self.invincible_period_time
            self.color = (255, 0, 0)
        
    def check_for_dead(self) -> bool:
        if self.health <= 0:
            return True # dead
        else:
            return False # alive
    
    def draw(self, screen):
        pygame.draw.polygon(surface=screen, color=self.color, points=self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if self.invincible_timer > 0:
            self.invincible_timer -= dt
            if self.invincible_timer <= 0:
                self.handle_invincible(switch=False)

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)

    def shoot(self, dt):
        self.shoot_cd_timer -= dt
        if self.shoot_cd_timer <= 0:
            bullet = Shot(self.position[0], self.position[1])
            bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.shoot_cd_timer = self.shoot_cd