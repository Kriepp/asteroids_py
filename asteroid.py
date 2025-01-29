import pygame
import random
from circleshape import *
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, asteroid_group):
        super().__init__(x , y, radius)
        self.asteroid_group = asteroid_group

    def draw(self, surface):
        pygame.draw.circle(surface, 'white', self.position, self.radius, width = 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        asteroid1 = self.velocity.rotate(random_angle)
        asteroid2 = self.velocity.rotate(-random_angle)
        radius = self.radius - ASTEROID_MIN_RADIUS
        first_asteroid = Asteroid(self.position.x, self.position.y, radius, self.asteroid_group)
        second_asteroid = Asteroid(self.position.x, self.position.y, radius, self.asteroid_group)
        first_asteroid.velocity = asteroid1 * 1.2
        second_asteroid.velocity = asteroid2 * 1.2
        self.asteroid_group.add(first_asteroid, second_asteroid)

        