import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from healthbar import Healthbar
from physics import resolve_collision, push_apart

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    FPS = 60
    running = True
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    entities = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable, entities)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable, entities)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    health_bar = Healthbar()


    while running:
        updatable.update(dt)
        asteroid_list = list(asteroids)
        for i in range(len(asteroid_list)):
            a1 = asteroid_list[i]
            for j in range(i + 1, len(asteroid_list)):
                a2 = asteroid_list[j]
                if a1.check_collide(a2):
                    resolve_collision(a1, a2)
                    push_apart(a1, a2)

        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.check_collide(bullet):
                    asteroid.get_hit(player.damage)
                    bullet.kill()
            if asteroid.check_collide(player):
                player.get_hit(asteroid.damage)
                if player.check_for_dead():
                    print("Game over!")
                    exit()

        screen.fill((0, 0, 0))
        for sprite in drawable:
            sprite.draw(screen)
        for entity in entities:
            if entity == player:
                health_bar.draw(entity, 10, 10, screen, width=200)
            else:
                if entity.health < entity.max_health:
                    health_bar.draw(entity, entity.position[0] - entity.radius, entity.position[1] - entity.radius, screen, width=entity.radius * 2)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        dt = clock.tick(FPS) / 1000
        



if __name__ == "__main__":
    main()
