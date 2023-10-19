import pygame

from Game.components.enemy.enemy_manager import EnemyManager
from Game.utils.constants import FPS, BACKGROUND, ICON, TITLE, SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER
from Game.components.player.player import Player

class Game():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 2
        self.x_position_background = 0
        self.y_position_background = 0     
        self.player = Player()
        self.enemy_manager = EnemyManager()

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
    
    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.enemy_manager.update()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        pygame.display.flip()   #--> Actualiza la ventana.

    def draw_background(self):
        image = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_position_background, self.y_position_background))
        self.screen.blit(image, (self.x_position_background, self.y_position_background - image_height))
        if self.y_position_background >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_position_background, self.y_position_background - image_height))
            self.y_position_background = 0
        self.y_position_background += self.game_speed