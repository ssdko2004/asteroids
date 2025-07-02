import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    pass_count, fail_count = pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    starting_x = SCREEN_WIDTH / 2
    starting_y = SCREEN_HEIGHT / 2
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)
    player = Player(starting_x, starting_y)
    asteroid_field = AsteroidField()
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updateable.update(dt)

        for asteroid in asteroids:
            if (asteroid.has_collided(player)):
                print(f"Astroid position, x: {asteroid.position.x}, y: {asteroid.position.y}")
                print(f"Player position, x: {player.position.x}, y: {player.position.y}")
                print(f"Distance to: {asteroid.position.distance_to(player.position)}")
                print(f"Combined Radius: {asteroid.radius + player.radius - 1}")
                
                print("Game over!")
                return
            for shot in shots:
                if (asteroid.has_collided(shot)):
                    asteroid.split()
                    shot.kill()

        screen.fill("black")

        for item in drawable:
            item.draw(screen)


        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
