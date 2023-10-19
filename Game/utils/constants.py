import pygame
import os

TITLE = "SpaceShips Game"
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 600
FPS = 60
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
BACKGROUND = pygame.image.load(os.path.join(IMG_DIR, "Background/Track.png"))

PLAYER = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
BULLET_PLAYER = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BASIC_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
EASY_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))