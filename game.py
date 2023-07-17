import pygame
import constants as consts
from entities import Defender, Alien

pygame.init()

# Assets
defender_img = pygame.image.load("assets/defender.png")
alien_imgs = {
    1: pygame.image.load("assets/alien1.png"),
    2: pygame.image.load("assets/alien2.png"),
    3: pygame.image.load("assets/alien3.png")
}
ufo_img = pygame.image.load("assets/ufo.png")
game_logo = pygame.image.load("assets/game_logo.png")

# Initialize the display
screen = pygame.display.set_mode(consts.SCREEN_SIZE)
pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(game_logo)


# Functions
def disp_entities():
    player.display(screen)
    for row in alien_rows:
        for alien in row:
            alien.display(screen)


# Define entities
player = Defender(defender_img, consts.INITIAL_PLAYER_COORDINATES)

alien_x, alien_y = consts.INITIAL_ALIEN_COORDINATES
alien_rows = [
    [Alien(alien_imgs[i + 1], (alien_x + consts.ALIEN_HORIZONTAL_GAP * j, alien_y + consts.ALIEN_VERTICAL_GAP * i)) for
     j in range(consts.NUM_ALIENS_PER_ROW)]
    for i in range(consts.NUM_ALIEN_ROWS)]

# Define variables used in game loop
move_left = False
move_right = False
clock = pygame.time.Clock()

# Game loop
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

    disp_entities()
    pygame.display.update()

    clock.tick(consts.FPS)
