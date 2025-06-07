import pygame
import sys
from constants import *
from player import *
from circleshape import CircleShape
from Asteroid import Asteroid
from Asteroidfield import *
from shot import Shot


def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Shot.containers = (updatable, drawable, shots)
    Asteroid.containers = (updatable, drawable, asteroid)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, PLAYER_RADIUS)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
        updatable.update(dt)
    
                    
        for obj in asteroid:
            if player.check_collision(obj):
                sys.exit("Game Over!")
            
            for shot in shots: 
                if obj.check_collision(shot):
                    obj.split()
                    shot.kill()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000  

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
if __name__ == "__main__":
    main()
