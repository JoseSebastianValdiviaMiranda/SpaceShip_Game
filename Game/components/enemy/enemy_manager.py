import random
from Game.utils.constants import SCREEN_HEIGHT
from Game.components.enemy.enemy import Enemy

class EnemyManager():
    def __init__(self):
        self.enemies = []

    def update(self):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update()
            if enemy.image_rect.y >= SCREEN_HEIGHT:
                self.enemies.remove(enemy)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        enemy_random = random.randint(1, 2)
        if enemy_random == 2:
            x_enemy_movement = [60, 150]
            enemy_speed = 5
            enemy = Enemy(enemy_random, x_enemy_movement, enemy_speed)
        else:
            enemy = Enemy()

        if len(self.enemies) < 1:            
            self.enemies.append(enemy)