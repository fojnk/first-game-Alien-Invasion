import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # Создаёт фон и корабль
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_widht, ai_settings.screen_height))
    pygame.display.set_caption("alien invasion")
    play_button = Button(ai_settings, screen, "Play")
    ship = Ship(ai_settings, screen) # Создание корабля
    balls = Group() # создание группы шаров
    alien = Alien(ai_settings, screen) # создание пришельца
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, balls)
        if stats.game_active:
            ship.update()
            gf.update_balls(ai_settings, screen, stats, sb, ship, aliens, balls)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, balls)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, balls, play_button)
run_game()
