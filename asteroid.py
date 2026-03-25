import pygame

from circleshape import CircleShape
from constants import LINE_WIDTH

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



