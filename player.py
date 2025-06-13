import pygame
from constants import *
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.timer = 0.0
        self.rotation = 0
    
    def rotate(self, dt):
        pass

    def move(self, dt, direction):
        move_distance = pygame.Vector2(0, 2)
        if direction == "left":
            self.position += move_distance.rotate(90)
        if direction == "right":
            self.position += move_distance.rotate(270)
        if direction == "up":
            self.position += move_distance.rotate(180)
        if direction == "down":
            self.position += move_distance

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.move(dt, direction="left")
        if keys[pygame.K_d]:
            self.move(dt, direction="right")
        if keys[pygame.K_w]:
            self.move(dt, direction="up")
        if keys[pygame.K_s]:
            self.move(dt, direction="down")

        self.timer -= dt
    
    def shape(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation) * self.radius / 1.5
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward
        b = self.position + right
        c = self.position - forward
        d = self.position - right
        return [a, b, c, d]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.shape(), 2)