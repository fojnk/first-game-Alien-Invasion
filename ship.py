import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings,  screen):
        super(Ship, self).__init__()
        self.screen = screen
        # Загрузка изображения корабля и получение его прямоугольника
        self.ai_settings = ai_settings
        self.image_0 = pygame.image.load(r"D:\alien_invasion\ship.png")
        self.image = pygame.transform.scale(self.image_0, (85, 100))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Координаты появления нового корабля
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        # обновляет позицию корабля с учётом флага
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center


    def blitme(self):
        # Рисует корабль в координатах
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx



