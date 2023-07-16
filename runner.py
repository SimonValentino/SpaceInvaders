import pygame
import constants as consts

def draw_player(x, y):
    screen.blit(defender, (x, y))

pygame.init()

screen = pygame.display.set_mode(consts.INITIAL_SCREEN_SIZE)

# Initialize the display
pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(pygame.image.load("assets/game_logo.png"))

# Create player defender
defender = pygame.image.load("assets/defender.png")
player_x, player_y = consts.INITIAL_PLAYER_COORDINATES

# Define movement flags
move_left = False
move_right = False

run_game = True
while run_game:
    screen.fill(consts.INITIAL_SCREEN_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False

        # Key is pressed down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right = True
            elif event.key == pygame.K_LEFT:
                move_left = True

        # Key is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False
            elif event.key == pygame.K_LEFT:
                move_left = False

    # Update player position based on movement flags
    if move_right:
        player_x += consts.PLAYER_SPEED
    if move_left:
        player_x -= consts.PLAYER_SPEED

    draw_player(player_x, player_y)
    pygame.display.update()
