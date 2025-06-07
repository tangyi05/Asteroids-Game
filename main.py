import pygame
import sys
from constants import *
from player import *
from circleshape import CircleShape
from Asteroid import Asteroid
from Asteroidfield import *


def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()

    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroid)

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, PLAYER_RADIUS)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
        updatable.update(dt)
        screen.fill("black")

        for obj in asteroid:
            if player.check_collision(obj):
                sys.exit("Game Over!")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000  

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
if __name__ == "__main__":
    main()
