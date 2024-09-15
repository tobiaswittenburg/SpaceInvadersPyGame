import pygame

class SplashScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.big_font = pygame.font.Font('freesansbold.ttf', 64)
        self.button_font = pygame.font.Font('freesansbold.ttf', 24)
        self.button_rect = pygame.Rect(300, 400, 200, 50)

    def draw(self):
        self.screen.fill((0, 0, 0))  # Fülle den Bildschirm mit schwarzer Farbe
        headline = self.big_font.render("Pause", True, (255, 255, 255))
        self.screen.blit(headline, (250, 100))

        instructions = [
            "Use arrow keys to move",
            "Press SPACE to shoot",
            "Press ESC to pause"
        ]

        for i, instruction in enumerate(instructions):
            text = self.font.render(instruction, True, (255, 255, 255))
            self.screen.blit(text, (200, 200 + i * 40))

        pygame.draw.rect(self.screen, (255, 255, 255), self.button_rect)
        button_text = self.button_font.render("Continue game", True, (0, 0, 0))
        self.screen.blit(button_text, (self.button_rect.x + 20, self.button_rect.y + 10))

    def is_continue_button_clicked(self, mouse_pos):
        return self.button_rect.collidepoint(mouse_pos)