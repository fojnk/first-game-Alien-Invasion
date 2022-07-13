import pygame

class Settings():
    def __init__(self):
        # Настройки фона и скорости
        self.screen_widht = 1400
        self.screen_height = 1000
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 2
        self.screen_image_0 = pygame.image.load(r"D:\alien_invasion\bg_image.jpg")
        self.screen_image = pygame.transform.scale(self.screen_image_0, (self.screen_widht, self.screen_height))

        # Настройки летящего шара
        self.ball_speed_factor = 2
        self.ball_image_0 = pygame.image.load(r"D:\alien_invasion\ball.png")
        self.ball_scale = 30
        self.ball_image = pygame.transform.scale(self.ball_image_0, (self.ball_scale, self.ball_scale))
        self.ball_rect = self.ball_image.get_rect()
        self.balls_counter = 2

        # Настройки пришельцев
        self.alien_widht = 80
        self.alien_height = 80
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 50
        self.fleet_direction = 1

        # Настройки игры
        self.ship_limit = 3

        # Темп ускорения игры
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 2
        self.ball_speed_factor = 2
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.ball_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)


