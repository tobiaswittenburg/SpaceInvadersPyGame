import pygame

class Bullet:
    def __init__(self, image_path, start_x, start_y, size, y_change):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, size)
        self.x = start_x
        self.y = start_y
        self.y_change = y_change
        self.state = "ready"  # "ready" bedeutet, dass die Kugel nicht sichtbar ist

    def fire(self, x, y):
        self.state = "fire"
        self.x = x
        self.y = y

    def move(self):
        if self.state == "fire":
            self.y -= self.y_change
            if self.y <= 0:
                self.state = "ready"
                self.y = 480

    def draw(self, screen):
        if self.state == "fire":
            screen.blit(self.image, (self.x + 16, self.y + 10))