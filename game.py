import pygame
import constants as consts
from entities import Player, Alien, Bullet
from screen_displays import Hud

pygame.init()

# Assets
player_img = pygame.image.load("assets/icons/player.png")
alien_img_states = [
    [pygame.image.load("assets/icons/alien1_state1.png"), pygame.image.load("assets/icons/alien1_state2.png")],
    [pygame.image.load("assets/icons/alien2_state1.png"), pygame.image.load("assets/icons/alien2_state2.png")],
    [pygame.image.load("assets/icons/alien3_state1.png"), pygame.image.load("assets/icons/alien3_state2.png")]
]
ufo_img = pygame.image.load("assets/icons/ufo.png")
game_logo = pygame.image.load("assets/icons/game_logo.png")
bullet_img = pygame.image.load("assets/icons/bullet.png")

# Initialize the display
screen = pygame.display.set_mode(consts.SCREEN_SIZE)
pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(game_logo)

# Define variables used in game loop
#   Movement flags
move_left = False
move_right = False

#   These variables will change based off the __level number
current_level = 1
num_alien_rows = consts.BASE_NUM_ALIEN_ROWS
alien_moves_per_second = consts.BASE_ALIEN_MOVES_PER_SECOND

#   Entities
player = Player(player_img, consts.INITIAL_PLAYER_COORDINATES)
bullet = Bullet(bullet_img, (0, 0))

alien_x, alien_y = consts.INITIAL_ALIEN_COORDINATES
alien_rows = [
    [Alien(alien_img_states[i % len(alien_img_states)],
           (alien_x + consts.ALIEN_HORIZONTAL_GAP * j, alien_y + consts.ALIEN_VERTICAL_GAP * i)) for
     j in range(consts.NUM_ALIENS_PER_ROW)]
    for i in range(num_alien_rows)]

#   Game displays
hud = Hud()

#   Time management
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
delta_time = 0

# Game loop
run_game = True
while run_game:
    delta_time = pygame.time.get_ticks() - start_time

    screen.fill((0, 0, 0))

    # Input checking
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False

        # Key is pressed down
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right = True
            elif event.key == pygame.K_LEFT:
                move_left = True
            elif event.key == pygame.K_SPACE and not bullet.is_active:
                bullet.fire((player.x, player.y))

        # Key is released
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False
            elif event.key == pygame.K_LEFT:
                move_left = False

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
            alien_moves_per_second *= consts.ALIEN_SPEED_SCALE * current_level

        start_time = pygame.time.get_ticks()

    # Move and update the bullet
    bullet.move()
    if not bullet.in_bounds():
        bullet.is_active = False

    # Collision detection between bullet and aliens
    for row in alien_rows:
        for alien in row:
            if bullet.is_active and bullet.collides_with(alien):
                bullet.is_active = False
                alien.kill()
                hud.update_score(consts.NUM_POINTS_FOR_ALIEN_KILL)

    # Remove the aliens that are set to remove
    for i in range(len(alien_rows)):
        alien_rows[i] = [alien for alien in alien_rows[i] if not alien.set_to_remove]

    # Display the entities
    player.display(screen)
    for row in alien_rows:
        for alien in row:
            alien.display(screen)

    # Display the bullet if active
    if bullet.is_active:
        bullet.display(screen)

    hud.display(screen)

    pygame.display.update()

    clock.tick(consts.FPS)
