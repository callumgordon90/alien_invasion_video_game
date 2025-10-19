import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        """Initialise the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        
        info = pygame.display.Info()
        self.screen = pygame.display.set_mode((info.current_w, info.current_h),pygame.NOFRAME)

        pygame.display.set_caption("Alien Invasion")

        #Importing the ship into the main game:
        self.ship = Ship(self)

        #Set the background colour.
        self.bg_color = (230, 230, 230)

    def run_game(self): 
        """Start the main loop for the game."""
        while True:
            #Call helper functions:
            self._check_events()
            self.ship.update()
            self._update_screen()


    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #Move the ship to the right.
                    self.ship.moving_right = True
                    #OR Move the ship to the left
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self): 
        """Update images on the screen, and flip to the new screen."""
         # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        #display the ship:
        self.ship.blitme()
            
        # Make the most recently drawn screen visable.
        pygame.display.flip()


#note: This if clause is inside the class
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()


    