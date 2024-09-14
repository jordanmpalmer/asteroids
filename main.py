# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import asteroid
from asteroid import Asteroid
from asteroidfield import *
from constants import *
from player import *
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updateable, drawable)
    Shot.containers = (shots, updateable, drawable)
    AsteroidField.containers = (updateable)
    asteroid_field = AsteroidField()

    Player.containers = (updateable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    dt = 0

    while True:
        # Close window if exit button clicked
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        if pygame.key.get_pressed()[pygame.K_q]:
            return

        # Draw single color to screen buffer
        screen.fill('black')

        # Update and draw for objects that have those groups
        for obj in updateable:
            obj.update(dt)

        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                return

            for shot in shots:
                if shot.check_collision(asteroid):
                    shot.kill()
                    asteroid.split()

        for obj in drawable:
            obj.draw(screen)

        # switch buffers
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()

