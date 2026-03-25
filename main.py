import pygame
import sys

from logger import log_state, log_event
from constants import * 

from player import Player
from asteroid import Asteroid 
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH} Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    Shot.containers = (shots, drawable, updatable)

    asteroidField = AsteroidField()

    # Game loop
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        #player.draw(screen)
        #player.update(dt)

        updatable.update(dt)
        # iterate over asteroid group
        for i in asteroids:
            if i.collides_with(player):
                log_event("player_hit")
                print("Game Over")
                sys.exit()


        for i in drawable:
            i.draw(screen)
        pygame.display.flip()

        
        dt = clock.tick(60)/1000
        

if __name__ == "__main__":
    main()
