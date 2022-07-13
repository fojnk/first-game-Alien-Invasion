import sys
import pygame
from ball import Ball
from time import sleep
from alien import Alien

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, balls):
    # Обрабатывает нажатие клавиш и передвижение мыши
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, balls)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, balls, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, balls, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        aliens.empty()
        balls.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def check_keydown_events(event, ai_settings, screen, ship, balls):
    # Реагирует на зажатие клавиши
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_ball(ai_settings, screen, balls, ship)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    # Реагирует на отпускание клавиши
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, stats, sb, ship, aliens, balls, play_button):
    # Обновляет изображения на экране
    # screen.fill(ai_settings.bg_color) - заменяет на монотонный фон
    screen.blit(ai_settings.screen_image, (0, 0)) # Рисует изображение
    ship.blitme() # Обновляет изображение корабля
    sb.show_score()
    for ball in balls.sprites():
        ball.draw_ball()
    aliens.draw(screen)
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()


def update_balls(ai_settings, screen, stats, sb, ship, aliens, balls):
    balls.update()
    for ball in balls.copy():
        if ball.rect.bottom <= 0:
            balls.remove(ball)
    check_balls_collisions(ai_settings, screen, stats, sb, ship, aliens, balls)


def check_balls_collisions(ai_settings, screen, stats, sb, ship, aliens, balls):
    collisions = pygame.sprite.groupcollide(balls, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points
        sb.prep_score()
        check_high_score(stats, sb)
    if len(aliens) == 0:
        balls.empty()
        ai_settings.increase_speed()
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, ship, aliens)

def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

def fire_ball(ai_settings, screen, balls, ship):
    if len(balls) < ai_settings.balls_counter:
        new_ball = Ball(ai_settings, screen, ship)
        balls.add(new_ball)


def create_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, ai_settings.alien_widht)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(ai_settings, alien_widht):
    # Определяет количество пришельцев в одном ряду
    available_space_x = ai_settings.screen_widht - 2 * alien_widht
    number_aliens_x = int(available_space_x / (2 * alien_widht))
    return  number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_widht = ai_settings.alien_widht
    alien.x = alien_widht + 2 * alien_widht * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_rows(ai_settinds, ship_height, alien_height):
    # Определяет количество рядов пришельцев
    available_space_y = (ai_settinds.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def update_aliens(ai_settings, screen, stats, sb, ship, aliens, balls):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, balls)
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, balls)

def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_directions(ai_settings, aliens)
            break

def change_fleet_directions(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, balls):
    if stats.ship_left > 0:
        stats.ship_left -= 1
        sb.prep_ships()
        aliens.empty()
        balls.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False
    pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, balls):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, balls)
            break



