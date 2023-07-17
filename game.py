import pygame
import constants as consts
from entities import Defender, Alien

pygame.init()

# Assets
defender_img = pygame.image.load("assets/defender.png")
alien_img_states = [
    [pygame.image.load("assets/alien1_state1.png"), pygame.image.load("assets/alien1_state2.png")],
    [pygame.image.load("assets/alien2_state1.png"), pygame.image.load("assets/alien2_state2.png")],
    [pygame.image.load("assets/alien3_state1.png"), pygame.image.load("assets/alien3_state2.png")]
]
ufo_img = pygame.image.load("assets/ufo.png")
game_logo = pygame.image.load("assets/game_logo.png")

# Initialize the display
screen = pygame.display.set_mode(consts.SCREEN_SIZE)
pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(game_logo)

# Define variables used in game loop
# Movement flags
move_left = False
move_right = False

# These variables will change based off the level number
num_alien_rows = 3
alien_moves_per_second = 2

# Entities
player = Defender(defender_img, consts.INITIAL_PLAYER_COORDINATES)

alien_x, alien_y = consts.INITIAL_ALIEN_COORDINATES
alien_rows = [
    [Alien(alien_img_states[i % len(alien_img_states)],
           (alien_x + consts.ALIEN_HORIZONTAL_GAP * j, alien_y + consts.ALIEN_VERTICAL_GAP * i)) for
     j in range(consts.NUM_ALIENS_PER_ROW)]
    for i in range(num_alien_rows)]

clock = pygame.time.Clock()

start_time = pygame.time.get_ticks()
delta_time = 0

# Game loop
run_game = True
while run_game:
    delta_time = pygame.time.get_ticks() - start_time

    screen.fill(consts.BG_SCREEN_COLOR)

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

        start_time = pygame.time.get_ticks()

    # Display the entities
    player.display(screen)
    for row in alien_rows:
        for alien in row:
            alien.display(screen)

    pygame.display.update()

    clock.tick(consts.FPS)
