from circleshape import *
from constants import *
from shot import *
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
        
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "#2596be", self.triangle(), 2)
        
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        
    def update(self, dt):
        self.shoot_timer -= dt
        
        if (self.position.x <= PLAYER_EDGE_BUFFER):
            self.position.x = PLAYER_EDGE_BUFFER
        if (self.position.x >= SCREEN_WIDTH - PLAYER_EDGE_BUFFER):
            self.position.x = SCREEN_WIDTH - PLAYER_EDGE_BUFFER
        if (self.position.y <= PLAYER_EDGE_BUFFER):
            self.position.y = PLAYER_EDGE_BUFFER
        if (self.position.y >= SCREEN_HEIGHT - PLAYER_EDGE_BUFFER):
            self.position.y = SCREEN_HEIGHT - PLAYER_EDGE_BUFFER
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1)
        if keys[pygame.K_SPACE]:
            self.shoot()
            
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
    def shoot(self):
        if (self.shoot_timer > 0):
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y, self.radius)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED