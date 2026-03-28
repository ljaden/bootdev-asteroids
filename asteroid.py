import pygame
import random
from logger import log_state, log_event

from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, surface):
        pygame.draw.circle(surface , color="white", center=self.position, radius=self.radius, width=LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        # check min asteroid size
        if self.radius <= ASTEROID_MIN_RADIUS:
            print("BABY ASTEROID")
            return
        
        log_event("asteroid_split")
        r_split_direction = random.uniform(20,50)
        print(r_split_direction)

        first_asteroid_velocity = self.velocity.rotate(r_split_direction)
        second_asteroid_velocity = self.velocity.rotate(r_split_direction * -1)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        #Asteroid(new_radius, (self.x,self.y), first_asteroid )
        a = Asteroid(self.position.x,self.position.y, new_radius)
        a.velocity = first_asteroid_velocity * 1.2
        
        b = Asteroid(self.position.x,self.position.y, new_radius)
        b.velocity = second_asteroid_velocity * 1.2

        print("BIG ASTEROID")
