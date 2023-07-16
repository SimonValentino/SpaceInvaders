import pygame
import constants as consts


def draw_player(x, y):
    screen.blit(defender, (x, y))


pygame.init()

# Assets
defender = pygame.image.load("assets/defender.png")
alien1 = pygame.image.load("assets/alien1.png")
alien2 = pygame.image.load("assets/alien2.png")
alien3 = pygame.image.load("assets/alien3.png")
alien4 = pygame.image.load("assets/alien4.png")
game_logo = pygame.image.load("assets/game_logo.png")

# Initialize the display
screen = pygame.display.set_mode(consts.SCREEN_SIZE)
pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(game_logo)

# Set characters coordinates
player_x, player_y = consts.INITIAL_PLAYER_COORDINATES

# Define movement flags
move_left = False
move_right = False

clock = pygame.time.Clock()

run_game = True
while run_game:
    screen.fill(consts.INITIAL_SCREEN_COLOR)

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
    pygame.display.update()

    clock.tick(consts.FPS)
