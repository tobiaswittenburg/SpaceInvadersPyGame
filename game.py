from SpaceInvaders import SpaceInvaders

class Game:

    def __init__(self) -> None:
        self.si = SpaceInvaders()


    def run(self):
        self.si.runGame()

        
if __name__ == "__main__":
    game = Game()
    game.run()