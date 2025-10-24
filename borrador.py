def _update_bullets(self):
        """Update the position of bullets and get rid of old bullets."""
        #Update bullet positions.
        self.bullets.update()
        
        #Get rid of bullets that have disappeared:
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            # print(len(self.bullets))

        #Check for any bullets that have hit aliens.
        #If so, get rid of the bullet and the alien:
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            #Destroy eisting bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
