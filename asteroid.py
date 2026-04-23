import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


def create_and_rotate_asteroid(x, y, angle, old_radius, old_velocity, speed):
    asteroid = Asteroid(x, y, old_radius - ASTEROID_MIN_RADIUS)
    asteroid.velocity = old_velocity.rotate(angle) * speed
    return asteroid


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        create_and_rotate_asteroid(
            self.position.x, self.position.y, angle, self.radius, self.velocity, 1.2
        )
        create_and_rotate_asteroid(
            self.position.x, self.position.y, -angle, self.radius, self.velocity, 1.2
        )
