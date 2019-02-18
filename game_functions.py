import sys
import pygame
from bullet import Bullet

def check_keydown_events (event,ai_settings,screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen,ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet (ai_settings,screen, ship, bullets):
    """Cоздание новой пули и в ключнение ее в гурппу"""
    if len(bullets) < ai_settings.bullets_allower:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events (event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings,screen, ship, bullets):
    """обрабатывает нажатие клавиш клавиатуры и мыши"""
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def updete_screen (ai_settings, screen, ship, alien, bullets):
    """перерисовка экрана при каджом действии"""
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitame()
    alien.blitme()

def update_bullets(bullets):
    """обновляет позиции пули и уничтажает старые пули"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

