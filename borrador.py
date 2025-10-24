def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        if self.play_button.rect.collidepoint(mouse_pos):
            #Reset the game statistics:
            self.stats.reset_stats()
            self.stats.game_active = True

            #Get rid of any remaining aliens and bullets:
            self.aliens.empty()
            self.bullets.empty()

            #Create a new fleet and center the ship:
            self._create_fleet()
            self.ship.center_ship()