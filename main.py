# Example file showing a basic pygame "game loop"
import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):
        # pygame setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        self.clock = pygame.time.Clock()
        self.level = Level()

    #boiler plate for the game window to run
    def run(self):
        while True:
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill("black")

            # RENDER YOUR GAME HERE
            self.level.run()

            pygame.display.update()
            self.clock.tick(60)  # limits FPS to 60
        
if __name__ == '__main__':
    game = Game()
    game.run()