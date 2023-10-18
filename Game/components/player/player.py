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

        if user_input[pygame.K_UP]: #--> UP(SUBIR)
            if self.image_rect.top > SCREEN_HEIGHT//2:
                self.image_rect.y -= self.SHIP_SPEED
            if user_input[pygame.K_LEFT]:
                self.image_rect.x -= self.SHIP_SPEED            
                if self.image_rect.left < 0:
                    self.image_rect.right = SCREEN_WIDTH
            elif user_input[pygame.K_RIGHT]:
                self.image_rect.x += self.SHIP_SPEED            
                if self.image_rect.right >= SCREEN_WIDTH:
                    self.image_rect.left = 0                                       
        elif user_input[pygame.K_DOWN]: #--> DOWN(BAJAR)
            if self.image_rect.bottom < SCREEN_HEIGHT:
                self.image_rect.y += self.SHIP_SPEED
            if user_input[pygame.K_LEFT]:
                self.image_rect.x -= self.SHIP_SPEED            
                if self.image_rect.left < 0:
                    self.image_rect.right = SCREEN_WIDTH
            elif user_input[pygame.K_RIGHT]:
                self.image_rect.x += self.SHIP_SPEED            
                if self.image_rect.right >= SCREEN_WIDTH:
                    self.image_rect.left = 0
        elif user_input[pygame.K_LEFT]: #--> LEFT(IZQUIERDA)
            self.image_rect.x -= self.SHIP_SPEED            
            if self.image_rect.left < 0:
                self.image_rect.right = SCREEN_WIDTH
        elif user_input[pygame.K_RIGHT]: #--> RIGHT(DERECHA)
            self.image_rect.x += self.SHIP_SPEED
            if self.image_rect.right >= SCREEN_WIDTH:
                self.image_rect.left = 0


    def draw(self, screen):
        #screen.blit(self.image, self.image_rect)
        screen.blit(self.image, (self.image_rect.x, self.image_rect.y))