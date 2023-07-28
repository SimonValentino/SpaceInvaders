import pygame
from constants import *
from entities import Player, Alien, PlayerBullet, AlienBullet, UFO
from screen_displays import Hud, game_over_screen
import random

pygame.init()

# Assets
player_img = pygame.image.load("assets/icons/player.png")
player_death_state = pygame.image.load("assets/icons/player_death.png")
player_bullet_img = pygame.image.load("assets/icons/player_bullet.png")

alien_img_states = [
    [pygame.image.load("assets/icons/alien1_state1.png"), pygame.image.load("assets/icons/alien1_state2.png")],
    [pygame.image.load("assets/icons/alien2_state1.png"), pygame.image.load("assets/icons/alien2_state2.png")],
    [pygame.image.load("assets/icons/alien3_state1.png"), pygame.image.load("assets/icons/alien3_state2.png")]
]
alien_death_states = [
    pygame.image.load("assets/icons/alien_death_state1.png"),
    pygame.image.load("assets/icons/alien_death_state2.png"),
    pygame.image.load("assets/icons/alien_death_state3.png")
]
alien_bullet_states = [
    pygame.image.load("assets/icons/alien_bullet_state1.png"),
    pygame.image.load("assets/icons/alien_bullet_state1.png"),
    pygame.image.load("assets/icons/alien_bullet_state2.png"),
    pygame.image.load("assets/icons/alien_bullet_state2.png")
]

ufo_img = pygame.image.load("assets/icons/ufo.png")
ufo_death_states = [
    pygame.image.load("assets/icons/ufo_death_state1.png"),
    pygame.image.load("assets/icons/ufo_death_state1.png"),
    pygame.image.load("assets/icons/ufo_death_state1.png"),
    pygame.image.load("assets/icons/ufo_death_state1.png"),
    pygame.image.load("assets/icons/ufo_death_state1.png"),
    pygame.image.load("assets/icons/ufo_death_state2.png"),
    pygame.image.load("assets/icons/ufo_death_state2.png"),
    pygame.image.load("assets/icons/ufo_death_state2.png"),
    pygame.image.load("assets/icons/ufo_death_state2.png"),
    pygame.image.load("assets/icons/ufo_death_state2.png"),
    pygame.image.load("assets/icons/ufo_death_state3.png"),
    pygame.image.load("assets/icons/ufo_death_state3.png"),
    pygame.image.load("assets/icons/ufo_death_state3.png"),
    pygame.image.load("assets/icons/ufo_death_state3.png"),
    pygame.image.load("assets/icons/ufo_death_state3.png")
]

game_logo = pygame.image.load("assets/icons/game_logo.png")

# Initialize the display
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(game_logo)


# Functions
def define_alien_rows():
    global num_alien_rows
    
    alien_x, alien_y = INITIAL_ALIEN_COORDINATES
    return [
        [Alien(alien_img_states[i % len(alien_img_states)], alien_death_states,
               (alien_x + ALIEN_HORIZONTAL_GAP * j, alien_y + ALIEN_VERTICAL_GAP * i)) for
         j in range(NUM_ALIENS_PER_ROW)]
        for i in range(num_alien_rows)]


def restart_level():
    global player, hud

    hud.num_lives -= 1
    reset_player()
    ufo.deactivate()

    set_properties_based_off_level()


def display_game():
    global alien_rows, player, bullet, ufo

    player.display(screen)

    for row in alien_rows:
        for alien in row:
            alien.display(screen)

    if player_bullet.is_active:
        player_bullet.display(screen)

    for bullet in alien_bullets:
        bullet.display(screen)

    hud.display(screen)
    
    if ufo.is_active():
        ufo.display(screen)

    pygame.display.update()


def set_properties_based_off_level():
    global level, num_alien_rows, alien_moves_per_second, alien_chance_to_fire, alien_rows, alien_bullets, points_per_kill, points_per_ufo_kill, ufo

    new_num_alien_rows = BASE_NUM_ALIEN_ROWS + (level - 1) // NUM_LEVELS_TILL_NEW_ALIEN_ROW
    num_alien_rows = new_num_alien_rows if new_num_alien_rows <= MAX_NUM_ALIEN_ROWS else MAX_NUM_ALIEN_ROWS
    alien_moves_per_second = BASE_ALIEN_MOVES_PER_SECOND * ALIEN_LEVEL_BEATEN_MOVES_PER_SECOND_SCALE ** level
    alien_chance_to_fire *= ALIEN_CHANCE_TO_FIRE_SCALE

    alien_rows = define_alien_rows()
    alien_bullets = []
    
    ufo = UFO(ufo_img, ufo_death_states, INITIAL_UFO_COORDINATES)
    ufo.speed *= UFO_SPEED_SCALE ** level

    points_per_kill = BASE_POINTS_PER_KILL * level
    points_per_ufo_kill = BASE_POINTS_PER_UFO_KILL * level


def restart_game():
    global hud, level, num_alien_rows, alien_moves_per_second, points_per_kill, alien_chance_to_fire, game_over, points_per_ufo_kill

    game_over = False
    level = 1
    num_alien_rows = BASE_NUM_ALIEN_ROWS
    alien_moves_per_second = BASE_ALIEN_MOVES_PER_SECOND
    alien_chance_to_fire = BASE_ALIEN_CHANCE_TO_FIRE
    points_per_kill = BASE_POINTS_PER_KILL
    points_per_ufo_kill = BASE_POINTS_PER_UFO_KILL
    hud = Hud()

    set_properties_based_off_level()


def reset_player():
    global player, player_bullet

    player = Player(player_img, player_death_state, INITIAL_PLAYER_COORDINATES)
    player_bullet = PlayerBullet(player_bullet_img, (0, 0))


def clear_screen():
    global screen

    screen.fill((0, 0, 0))
    pygame.display.update()


# Define variables used in game loop
#   Movement flags
move_left = False
move_right = False

#   Game over flag
game_over = False

#   These variables will change based off the level number
level = 6
num_alien_rows = BASE_NUM_ALIEN_ROWS
alien_moves_per_second = BASE_ALIEN_MOVES_PER_SECOND
alien_chance_to_fire = BASE_ALIEN_CHANCE_TO_FIRE
points_per_kill = BASE_POINTS_PER_KILL
points_per_ufo_kill = BASE_POINTS_PER_UFO_KILL

#   Entities
player = Player(player_img, player_death_state, INITIAL_PLAYER_COORDINATES)
player_bullet = PlayerBullet(player_bullet_img, (0, 0))

alien_rows = define_alien_rows()
alien_bullets = []

ufo = UFO(ufo_img, ufo_death_states, INITIAL_UFO_COORDINATES)

#   Game displays
hud = Hud()

#   Time management
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
delta_time = 0

# Game loop
run_game = True

while run_game:
    if hud.num_lives <= 0:
        hud.update_high_score()
        hud.save_high_score()
        game_over = True

    # Check if level is beaten
    if not any(alien_rows) and not ufo.is_active():
        pygame.time.wait(3_000)
        level += 1
        hud.next_level()

        set_properties_based_off_level()
        reset_player()

    delta_time = pygame.time.get_ticks() - start_time

    screen.fill((0, 0, 0))

    # Input checking
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False

        # Key is pressed down
        elif event.type == pygame.KEYDOWN:
            if game_over:
                if event.key == pygame.K_r:
                    restart_game()

            else:
                if event.key == pygame.K_RIGHT:
                    move_right = True
                elif event.key == pygame.K_LEFT:
                    move_left = True
                elif event.key == pygame.K_SPACE and not player_bullet.is_active:
                    player_bullet.fire((player.x, player.y))

        # Key is released
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False
            elif event.key == pygame.K_LEFT:
                move_left = False

    if game_over:
        game_over_screen(screen, hud)
        pygame.display.update()
        continue

    # Update player position based on movement flags
    if move_right:
        player.move_right()
    elif move_left:
        player.move_left()

    # Move aliens
    if delta_time >= 1 / alien_moves_per_second * 1_000:
        drop_row = False
        for row in alien_rows:
            for alien in row:
                alien.move()
                if not alien.in_bounds():
                    drop_row = True

        if drop_row:
            for row in alien_rows:
                for alien in row:
                    alien.drop_row()
            alien_moves_per_second *= ALIEN_DROP_ROW_MOVES_PER_SECOND_SCALE

        start_time = pygame.time.get_ticks()

    # Alien shooting logic
    for row in alien_rows:
        for alien in row:
            if random.random() <= alien_chance_to_fire:
                bullet = AlienBullet(alien_bullet_states, (alien.x, alien.y))
                alien_bullets.append(bullet)

    # Move and update the alien bullets
    for bullet in alien_bullets:
        bullet.move()
        if not bullet.in_bounds():
            alien_bullets.remove(bullet)
        elif bullet.collides_with(player):
            # Collision detection between alien bullets and player
            player.kill()
            display_game()
            pygame.time.wait(3_000)
            restart_level()
    
    # UFO move and update
    ufo.check_appearance()
    ufo.move()

    # Move and update the player bullet
    player_bullet.move()
    if not player_bullet.in_bounds():
        player_bullet.is_active = False

    # Collision detection between player bullet and aliens
    for row in alien_rows:
        for alien in row:
            if player_bullet.is_active and player_bullet.collides_with(alien):
                player_bullet.is_active = False
                alien.kill()
                hud.score += points_per_kill
    
    # Collision detection between player bullet and UFO
    if ufo.is_active() and player_bullet.is_active and player_bullet.collides_with(ufo):
        player_bullet.is_active = False
        ufo.kill()
        hud.score += points_per_ufo_kill

    # Check for alien invasion
    #   Finding last alien
    for row in reversed(range(len(alien_rows))):
        for col in reversed(range(len(alien_rows[row]))):
            if alien_rows[row][col]:
                #   Invade if alien is over bounds
                if alien_rows[row][col].in_player_territory():
                    pygame.time.wait(2_000)
                    clear_screen()
                    alien_rows[row][col].invade(player)
                    player.kill()
                    alien_rows[row][col].display(screen)
                    player.display(screen)
                    hud.display(screen)
                    pygame.display.update()
                    pygame.time.wait(5_000)
                    restart_level()
                    break
                break

    # Remove the aliens that are set to remove
    for i in range(len(alien_rows)):
        alien_rows[i] = [alien for alien in alien_rows[i] if not alien.set_to_remove]
    
    if ufo.set_to_remove:
        ufo.deactivate()

    display_game()

    clock.tick(FPS)
