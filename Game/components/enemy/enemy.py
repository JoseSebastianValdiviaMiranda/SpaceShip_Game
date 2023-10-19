import pygame
import random

from pygame.sprite import Sprite
from Game.utils.constants import BASIC_ENEMY, EASY_ENEMY, SCREEN_WIDTH, SCREEN_HEIGHT

class Enemy(Sprite):
    #--> Size enemy.
    ENEMY_HEIGHT = 55
    ENEMY_WIDTH = 35    

    #--> Enemy Position        
    Y_POSITION_ENEMY = 0

    #--> Enemy movement.    
    ENEMY_MOVEMENT = {0:'left', 1:'right'}    

    #--> Enemy type.
    ENEMY_TYPE = {1:BASIC_ENEMY, 2:EASY_ENEMY}

    def __init__(self, enemy_type = 1, x_enemy_movement = [30, 100], enemy_speed = 4):
        self.image = pygame.transform.scale(self.ENEMY_TYPE[enemy_type], (self.ENEMY_WIDTH, self.ENEMY_HEIGHT))
        self.image_rect = self.image.get_rect()        
        self.image_rect.x = random.randrange(100, 1000, 50)
        self.image_rect.y = self.Y_POSITION_ENEMY
        self.movement = self.ENEMY_MOVEMENT[random.randint(0,1)]
        self.x_movement_enemy = random.randint(x_enemy_movement[0], x_enemy_movement[1])
        self.enemy_speed = enemy_speed
        self.index = 0

    def update(self):        
        self.image_rect.y += self.enemy_speed
        if self.movement == 'left':
            self.image_rect.x -= self.enemy_speed
        else:
            self.image_rect.x += self.enemy_speed
        self.change_movement()

    def change_movement(self):
        self.index += 1
        if (self.index >= self.x_movement_enemy) or (self.image_rect.left < 0) or (self.image_rect.right >= SCREEN_WIDTH):
            if self.movement == 'left':
                self.movement = 'right'
            elif self.movement == 'right':
                self.movement = 'left'
            self.index = 0

    def draw(self, screen):
        screen.blit(self.image, (self.image_rect.x, self.image_rect.y))