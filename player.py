import logging

import pygame

from circleshape import CircleShape
from constants import *
from shot import Shot


logger = logging.getLogger("asteroids.player")


class Player(CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x=x, y=y, radius=PLAYER_RADIUS)
        self.rotation = 180
        self.shoot_timer = 0

    def __repr__(self):
        return f"Player(pos={self.position}, rotation={self.rotation})"

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5

        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right

        return [a, b, c]

    def shoot(self):
        if self.shoot_timer > 0:
            return
        
        pos = self.triangle()[0]
        shot = Shot(pos.x, pos.y)

        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity = forward * PLAYER_SHOOT_SPEED
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN

    def draw(self, screen: pygame.Surface) -> pygame.Rect:
        pygame.draw.polygon(
            screen,
            (51, 255, 0),
            self.triangle(),
            2
        )

    def rotate(self, dt: float):
        logger.debug(f"player.rotate(dt={dt}): rotating {PLAYER_TURN_SPEED * dt} degrees")
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt: float):
        logger.debug(f"player.rotate(dt={dt}): player moving {'forward' if dt > 0 else 'backward'}")
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt: float):
        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            logger.debug("player.update(): `W` pressed")
            self.move(dt)

        if keys[pygame.K_a]:
            logger.debug("player.update(): `A` pressed")
            self.rotate(-dt)

        if keys[pygame.K_s]:
            logger.debug("player.update(): `S` pressed")
            self.move(-dt)

        if keys[pygame.K_d]:
            logger.debug("player.update(): `D` pressed")
            self.rotate(dt)

        if keys[pygame.K_SPACE]:
            logger.debug("player.update(): `SPACE` pressed")
            self.shoot()

        # wrap screen
        if self.position.x < -self.radius:
            self.position.x = SCREEN_WIDTH

        if self.position.x > SCREEN_WIDTH + self.radius:
            self.position.x = 0

        if self.position.y < -self.radius:
            self.position.y = SCREEN_HEIGHT

        if self.position.y > SCREEN_HEIGHT + self.radius:
            self.position.y = 0

