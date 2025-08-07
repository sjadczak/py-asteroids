import logging

import pygame

from circleshape import CircleShape
from constants import *


logger = logging.getLogger("asteroids.shot")


class Shot(CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(
            screen,
            (51, 255, 0),
            self.position,
            self.radius,
            0
        )

    def update(self, dt: float):
        self.position += (self.velocity * dt)

        # if shot is off screen, kill
        if (
            (self.position.x < -self.radius or self.position.x > SCREEN_WIDTH + self.radius) or
            (self.position.y < -self.radius or self.position.y > SCREEN_HEIGHT + self.radius)
        ):
            self.kill()
