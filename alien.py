import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    # Инициализация пришельца
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()

        self.screen = screen
        self.ai_settings = ai_settings
        # Добавление изображения и прямоугольника
        self.image_0 = pygame.image.load(r"D:\alien_invasion\alien.png")
        self.image = pygame.transform.scale(self.image_0, (ai_settings.alien_widht, ai_settings.alien_height))
        self.rect = self.image.get_rect()

        # Каждый новый пришелец появляется в левом верхнем углу (начало координат в левом верхнем углу)
        self.rect.x = self.rect.width / 2
        self.rect.y = self.rect.height / 2

        self.x = float(self.rect.x)

    def check_edges(self):
        # Возвращает True, если пришелец находится у края экрана
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x



