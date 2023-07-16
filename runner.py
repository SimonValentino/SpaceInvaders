import pygame
import constants as consts


pygame.init()

# Assets
defender = pygame.image.load("assets/defender.png")
alien1 = pygame.image.load("assets/alien1.png")
alien2 = pygame.image.load("assets/alien2.png")
alien3 = pygame.image.load("assets/alien3.png")
ufo = pygame.image.load("assets/ufo.png")
game_logo = pygame.image.load("assets/game_logo.png")

# Initialize the display
screen = pygame.display.set_mode(consts.SCREEN_SIZE)
pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(game_logo)


# Functions
def draw_player(x, y):
    screen.blit(defender, (x, y))


def draw_alien(alien, x, y):
    screen.blit(alien, (x, y))


# Define aliens
alien_rows = [
    [alien1] * consts.NUM_ALIENS_PER_ROW,
    [alien2] * consts.NUM_ALIENS_PER_ROW,
    [alien2] * consts.NUM_ALIENS_PER_ROW,
    [alien3] * consts.NUM_ALIENS_PER_ROW,
    [alien3] * consts.NUM_ALIENS_PER_ROW
]
alien_x = consts.ALIEN_START_X
alien_y = consts.ALIEN_START_Y


# Set characters coordinates
player_x, player_y = consts.INITIAL_PLAYER_COORDINATES

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
    if move_right and player_x <= consts.RIGHT_BOUND:
        player_x += consts.PLAYER_SPEED
    elif move_left and player_x >= consts.LEFT_BOUND:
        player_x -= consts.PLAYER_SPEED

    draw_player(player_x, player_y)

    # Draw aliens
    for row in range(len(alien_rows)):
        for col in range(len(alien_rows[row])):
            alien = alien_rows[row][col]
            draw_alien(alien, alien_x + col * consts.ALIEN_HORIZONTAL_GAP, alien_y + row * consts.ALIEN_VERTICAL_GAP)

    pygame.display.update()

    clock.tick(consts.FPS)
