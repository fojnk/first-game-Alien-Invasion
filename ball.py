import pygame
from pygame.sprite import Sprite

class Ball(Sprite):
    # Класс для управления шарами, выпущенными кораблём
    def __init__(self, ai_settings, screen, ship):
        # Создание объекта шара в текущей позиции корабля
        super(Ball, self).__init__() # Наследование от класса Sprite
        self.screen = screen

        # Создание шара и назначение правильной позиции
        self.image = ai_settings.ball_image
        self.rect = self.image.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top + 10

        # Позиция шара хранится в вещественных числах
        self.y = float(self.rect.y)

        self.speed_factor = ai_settings.ball_speed_factor

    def update(self):
        # Перемещение шара вверх по экрану
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_ball(self):
        # Выводит шар на экран
        self.screen.blit(self.image, self.rect)
