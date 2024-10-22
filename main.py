import pygame
from constants import *
from player import player

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0

	Player = player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		screen.fill("black")
		Player.update(dt)
		Player.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) / 1000
		

if __name__ == "__main__": #runs when the file is run directly
	main()
