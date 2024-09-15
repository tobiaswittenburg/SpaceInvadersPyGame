import pygame
import random

class Enemy:
    def __init__(self, image_path, screen_width, screen_height):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (50, 50))  # Skaliere das Gegner-Bild
        self.x = random.randint(0, screen_width - 50)
        self.y = random.randint(50, 150)
        self.x_change = 4
        self.y_change = 40
        self.screen_width = screen_width
        self.screen_height = screen_height

    def move(self):
        self.x += self.x_change
        if self.x <= 0 or self.x >= self.screen_width - 50:
            self.x_change = -self.x_change
            self.y += self.y_change

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def reset_position(self):
        self.x = random.randint(0, self.screen_width - 50)
        self.y = random.randint(50, 150)