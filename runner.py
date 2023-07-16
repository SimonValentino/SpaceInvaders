import pygame
import constants as consts


def draw_player():
    screen.blit(defender, (player_x, player_y))


pygame.init()

screen = pygame.display.set_mode(consts.INITIAL_SCREEN_SIZE, pygame.RESIZABLE)

# Initialize the display
pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(pygame.image.load("assets/game_logo.png"))

# Create player defender
defender = pygame.image.load("assets/defender.png")
player_x, player_y = consts.INITIAL_PLAYER_COORDINATES

run_game = True
while run_game:
    screen.fill(consts.INITIAL_SCREEN_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False

    draw_player()
    pygame.display.update()
