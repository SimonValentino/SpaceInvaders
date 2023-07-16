import pygame
import constants as consts
from entities import Defender, Alien


pygame.init()

# Assets
defender_img = pygame.image.load("assets/defender.png")
alien1_img = pygame.image.load("assets/alien1.png")
alien2_img = pygame.image.load("assets/alien2.png")
alien3_img = pygame.image.load("assets/alien3.png")
ufo_img = pygame.image.load("assets/ufo.png")
game_logo = pygame.image.load("assets/game_logo.png")

# Initialize the display
screen = pygame.display.set_mode(consts.SCREEN_SIZE)
pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(game_logo)

# Define entities
player = Defender(defender_img, consts.INITIAL_PLAYER_COORDINATES)


# Define movement flags
move_left = False
move_right = False

clock = pygame.time.Clock()

run_game = True
while run_game:
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
    if move_right and player.in_right_bound():
        player.move_right()
    elif move_left and player.in_left_bound():
        player.move_left()

    player.display(screen)

    pygame.display.update()

    clock.tick(consts.FPS)
