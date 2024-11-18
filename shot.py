from circleshape import *
from constants import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "#be2fb7", self.position, self.radius, SHOT_RADIUS)
        
    def update(self, dt):
        self.position += self.velocity * dt