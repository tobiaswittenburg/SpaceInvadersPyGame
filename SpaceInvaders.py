import pygame  # Importiere das Pygame-Modul
import random  # Importiere das Random-Modul für zufällige Positionen
from SplashScreen import SplashScreen  # Importiere die SplashScreen-Klasse
from Enemy import Enemy  # Importiere die Enemy-Klasse

class SpaceInvaders:

    BLACK = (0,0,0)
    PLAYER_SIZE = (20,40)
    ENEMY_SIZE = (40,30)
    BULLET_SIZE = (20,20)
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    def __init__(self):
        self.initPyGame()
        self.initGame()

    def initPyGame(self):
        # Initialisiere Pygame
        pygame.init()

        # Setze die Bildschirmgröße
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()  # Erstelle eine Clock-Instanz
        self.splashScreen = SplashScreen(self.screen)  # Erstelle eine SplashScreen-Instanz

        # Titel und Icon
        pygame.display.set_caption("Space Invaders")
        self.icon = pygame.image.load('img/player.png')  # Lade das Icon-Bild
        pygame.display.set_icon(self.icon)

    def initGame(self):
        # Spieler
        self.playerImg = pygame.image.load('img/player.png')  # Lade das Spieler-Bild
        self.playerImg = pygame.transform.scale(self.playerImg, self.PLAYER_SIZE)
        self.playerX = 370  # Anfangsposition des Spielers auf der X-Achse
        self.playerY = 480  # Anfangsposition des Spielers auf der Y-Achse
        self.playerX_change = 0  # Bewegung des Spielers auf der X-Achse
        self.playerY_change = 0

        # Gegner
        self.enemyImg = []
        self.enemyX = []
        self.enemyY = []
        self.enemyX_change = []
        self.enemyY_change = []
        self.num_of_enemies = 6  # Anzahl der Gegner

        self.enemies = [Enemy('img/enemy.png', self.SCREEN_WIDTH, self.SCREEN_HEIGHT) for _ in range(6)]

        # Kugel
        self.bulletImg = pygame.image.load('img/bullet.png')  # Lade das Kugel-Bild
        self.bulletImg = pygame.transform.scale(self.bulletImg, self.BULLET_SIZE)
        self.bulletX = 0  # Anfangsposition der Kugel auf der X-Achse
        self.bulletY = 480  # Anfangsposition der Kugel auf der Y-Achse
        self.bulletX_change = 0  # Bewegung der Kugel auf der X-Achse
        self.bulletY_change = 10  # Bewegung der Kugel auf der Y-Achse
        self.bullet_state = "ready"  # Zustand der Kugel ("ready" bedeutet, dass die Kugel nicht sichtbar ist)

        # Punkte
        self.score_value = 0  # Anfangswert der Punkte
        self.font = pygame.font.Font('freesansbold.ttf', 32)  # Schriftart und -größe für die Punkteanzeige
        self.textX = 10  # X-Position der Punkteanzeige
        self.textY = 10  # Y-Position der Punkteanzeige

        # Spielende Text
        self.over_font = pygame.font.Font('freesansbold.ttf', 64)  # Schriftart und -größe für das Spielende

    def showScore(self, x, y):
        self.score = self.font.render("Score : " + str(self.score_value), True, (255, 255, 255))  # Rendern des Punktestands
        self.screen.blit(self.score, (x, y))  # Zeichnen des Punktestands auf dem Bildschirm

    def drawGameOverText(self):
        self.over_text = self.over_font.render("GAME OVER", True, (255, 255, 255))  # Rendern des Spielende-Textes
        self.screen.blit(self.over_text, (200, 250))  # Zeichnen des Spielende-Textes auf dem Bildschirm
        

    def drawPlayer(self, x, y):
        self.screen.blit(self.playerImg, (x, y))  # Zeichnen des Spielers auf dem Bildschirm

    def fire_bullet(self):
        self.bulletX = self.playerX  # Setze die Kugelposition auf die Spielerposition
        self.bulletY = self.playerY
        global bullet_state
        bullet_state = "fire"  # Ändere den Zustand der Kugel zu "fire"
        self.screen.blit(self.bulletImg, (self.bulletX + 16, self.bulletY + 10))  # Zeichnen der Kugel auf dem Bildschirm

    def moveBullet(self):
        self.bulletY -= self.bulletY_change  # Bewege die Kugel nach oben

    def movePlayer(self):
        # Aktualisiere die Spielerposition
        self.playerX += self.playerX_change  
        self.playerY += self.playerY_change

        if self.playerX <= 0:
            self.playerX = 0  # Begrenze die Spielerposition auf der linken Seite
        elif self.playerX >= self.SCREEN_WIDTH:
            self.playerX = self.SCREEN_WIDTH-20  # Begrenze die Spielerposition auf der rechten Seite

        if self.playerY <= 0:
            self.playerY = 0
        elif self.playerY >= self.SCREEN_HEIGHT - 20:
            self.playerY = self.SCREEN_HEIGHT - 20

    def isCollision(self, enemyX, enemyY, bulletX, bulletY):
        distance = ((enemyX - bulletX)**2 + (enemyY - bulletY)**2)**0.5  # Berechnung der Entfernung zwischen Kugel und Gegner
        if distance < 27:
            return True  # Kollision erkannt
        else:
            return False  # Keine Kollision

    def runGame(self):
        # Hauptspiel-Schleife
        running = True
        pause = False
   
        while running:
            self.screen.fill(self.BLACK)  # Fülle den Bildschirm mit schwarzer Farbe
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Überprüfe, ob das Spiel beendet werden soll
                    running = False

                if event.type == pygame.KEYDOWN:  # Überprüfe, ob eine Taste gedrückt wurde
                    if event.key == pygame.K_ESCAPE:  # Überprüfe, ob die Escape-Taste gedrückt wurde
                        pause = True  # Setze die Pause-Variable auf True

                    if not pause:
                        if event.key == pygame.K_LEFT:  # Überprüfe, ob die linke Pfeiltaste gedrückt wurde
                            self.playerX_change = -5  # Bewege den Spieler nach links
                        if event.key == pygame.K_RIGHT:  # Überprüfe, ob die rechte Pfeiltaste gedrückt wurde
                            self.playerX_change = 5  # Bewege den Spieler nach rechts
                        if event.key == pygame.K_UP:
                            self.playerY_change = -5
                        if event.key == pygame.K_DOWN:
                            self.playerY_change = 5
                        if event.key == pygame.K_SPACE:  # Überprüfe, ob die Leertaste gedrückt wurde
                            if self.bullet_state == "ready":
                                self.fire_bullet()  # Feuere die Kugel ab
                      
                if event.type == pygame.KEYUP:  # Überprüfe, ob eine Taste losgelassen wurde
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.playerX_change = 0  # Stoppe die Bewegung des Spielers
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        self.playerY_change = 0

                if event.type == pygame.MOUSEBUTTONDOWN: 
                    if pause:
                        if self.splashScreen.is_continue_button_clicked(event.pos):
                            pause = False
                    else:
                        if self.bullet_state == "ready":
                            self.fire_bullet()  # Feuere die Kugel ab

            if not pause:
                self.movePlayer()
                self.moveBullet()
                # self.moveEnemies()

                for enemy in self.enemies:
                    enemy.move()
                    if enemy.y > 440:
                        for e in self.enemies:
                            e.y = 2000  # Bewege alle Gegner aus dem Bildschirm
                        self.drawGameOverText()  # Zeige den Spielende-Text
                        break

                    collision = self.isCollision(enemy.x, enemy.y, self.bulletX, self.bulletY)  # Überprüfe auf Kollision
                    if collision:
                        self.bulletY = 480  # Setze die Kugelposition zurück
                        self.bullet_state = "ready"  # Setze den Kugelzustand zurück
                        self.score_value += 1  # Erhöhe den Punktestand
                        enemy.reset_position()  # Setze die Gegnerposition zurück

                    enemy.draw(self.screen)  # Zeichne den Gegner



                if self.bulletY <= 0:
                    self.bulletY = 480  # Setze die Kugelposition zurück
                    self.bullet_state = "ready"  # Setze den Kugelzustand zurück

                if self.bullet_state == "fire":
                    self.fire_bullet(self.bulletX, self.bulletY)  # Feuere die Kugel ab
                    self.moveBullet()

                self.drawPlayer(self.playerX, self.playerY)  # Zeichne den Spieler
                self.showScore(self.textX, self.textY)  # Zeige den Punktestand
            else:
                self.splashScreen.draw()

            pygame.display.update()  # Aktualisiere den Bildschirm
            self.clock.tick(60)