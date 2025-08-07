import logging
import random

import pygame

from circleshape import CircleShape
from constants import *


logger = logging.getLogger("asteroids.asteroid")


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x=x, y=y, radius=radius)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            self.position,
            self.radius,
            2
        )

    def update(self, dt: float):
        self.position += self.velocity * dt

        # if asteroid is off screen, kill
        if (
            (self.position.x < -self.radius or self.position.x > SCREEN_WIDTH + self.radius) or
            (self.position.y < -self.radius or self.position.y > SCREEN_HEIGHT + self.radius)
        ):
            self.kill()

    def split(self):
        # Asteroid is always killed, some spawn replacements
        self.kill()

        # Small asteroids just get destroyed
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        left = self.velocity.rotate(-random_angle)
        right = self.velocity.rotate(random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        left_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        left_asteroid.velocity = left * ASTEROID_SPEED_MULTIPLIER

        right_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        right_asteroid.velocity = right * ASTEROID_SPEED_MULTIPLIER

