import pygame


# Base Class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, radius: int):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity: pygame.Vector2 = pygame.Vector2(0, 0)
        self.radius: int = radius

    def is_colliding(self, other):
        return self.position.distance_to(other.position) < self.radius + other.radius

    def draw(self, screen: pygame.Surface):
        raise NotImplementedError("Subclass must implement `draw`")

    def update(self, dt):
        raise NotImplementedError("Subclass must implement `update`")
