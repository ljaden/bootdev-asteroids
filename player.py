import pygame

from circleshape import CircleShape
from shot import Shot

from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS

class Player(CircleShape):
    def __init__(self, x,y):
        super().__init__(x,y, PLAYER_RADIUS)

        self.x = x
        self.y = y
        self.rotation = 0
        self.shot_cooldown = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self,screen):
        pygame.draw.polygon(screen,"white",self.triangle(),LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        # A key -- move left 
        if keys[pygame.K_a]:
            self.rotate(dt*-1)

        # d key -- move right
        if keys[pygame.K_d]:
            self.rotate(dt)

        # W key -- move up
        if keys[pygame.K_w]:
            self.move(dt)
        # S key -- move down
        if keys[pygame.K_s]:
            self.move(dt*-1)

        # SPACE key -- fires shot
        if keys[pygame.K_SPACE]:
            self.shoot()

        # reduce shot_cooldown by dt(delta time)
        self.shot_cooldown -= dt

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        if self.shot_cooldown > 0:
            return
        else:
            self.shot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS

        bullet = Shot(self.position.x, self.position.y)
        bullet.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

