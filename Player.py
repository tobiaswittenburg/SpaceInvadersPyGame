import pygame

class Player:
    def __init__(self, image_path, start_x, start_y, size, screen_width, screen_height):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, size)
        self.x = start_x
        self.y = start_y
        self.x_change = 0
        self.y_change = 0
        self.screen_width = screen_width   
        self.screen_height = screen_height 

    def move(self, changeX, changeY):
        self.x += changeX
        self.y += changeY


        # Begrenze die Spielerposition auf dem Bildschirm
        if self.x <= 0:
            self.x = 0
        elif self.x >= self.screen_width - self.image.get_width():
            self.x = self.screen_width - self.image.get_width()

        if self.y <= 0:
            self.y = 0
        elif self.y >= self.screen_height - self.image.get_height():
            self.y = self.screen_height - self.image.get_height()

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))