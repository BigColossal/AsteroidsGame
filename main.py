import sys
import pygame
from gameobjects.player import Player
from gameobjects.asteroid import Asteroid
from gameobjects.asteroidfield import AsteroidField
from gameobjects.shot import Shot
from gameobjects.coin import Coin
from coincounter import CoinCounter

pygame.init()
from constants import *

def main():
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	coins = pygame.sprite.Group()
	coinCoint = pygame.sprite.Group()

	Asteroid.containers = (asteroids, updatable, drawable)
	Shot.containers = (shots, updatable, drawable)
	AsteroidField.containers = updatable
	Coin.containers = (coins, drawable)
	CoinCounter.containers = (updatable, drawable)
	asteroid_field = AsteroidField()
	coin_count = CoinCounter()

	Player.containers = (updatable, drawable)

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	dt = 0

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		for object in updatable:
			object.update(dt)

		for asteroid in asteroids:
			if asteroid.collides_with(player):
				print("Game over!")
				sys.exit()

			for shot in shots:
				if asteroid.collides_with(shot):
					asteroid.split(screen)
					shot.kill()

		for coin in coins:
			if player.collides_with(coin):
				coin_count.add_value(coin)
				coin.kill()

		screen.fill("black")

		for object in drawable:
			object.draw(screen)

		pygame.display.flip()

		dt = clock.tick(60) / 1000 #limits the fps to 60 frames per second
		

if __name__ == "__main__": #runs when the file is run directly
	main()
