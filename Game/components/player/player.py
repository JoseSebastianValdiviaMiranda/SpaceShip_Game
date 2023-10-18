import pygame

from pygame.sprite import Sprite
from Game.utils.constants import PLAYER, SCREEN_WIDTH, SCREEN_HEIGHT

class Player(Sprite):
    #--> Ship size.
    SHIP_HEIGHT = 55
    SHIP_WIDTH = 35

    #--> Ship speed.
    SHIP_SPEED = 10

    #--> Ship position.
    X_POSITION_SHIP = SCREEN_WIDTH//2 - SHIP_WIDTH//2
    Y_POSITION_SHIP = SCREEN_HEIGHT - SHIP_HEIGHT

    def __init__(self):
        self.image = pygame.transform.scale(PLAYER, (self.SHIP_WIDTH, self.SHIP_HEIGHT))                
        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.X_POSITION_SHIP
        self.image_rect.y = self.Y_POSITION_SHIP

    def update(self, user_input):
        if user_input[pygame.K_LEFT]:
            self.image_rect.x -= self.SHIP_SPEED       

    def draw(self, screen):
        #screen.blit(self.image, self.image_rect)
        screen.blit(self.image, (self.image_rect.x, self.image_rect.y))