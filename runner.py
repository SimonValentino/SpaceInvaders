import pygame
import constants as consts


def init_disp():
    pygame.display.set_caption("Space Invaders")
    pygame.display.set_icon(pygame.image.load("assets/game_logo.png"))


pygame.init()
screen = pygame.display.set_mode(consts.INITIAL_SCREEN_SIZE, pygame.RESIZABLE)

run_game = True
while run_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False

    screen.fill(consts.INITIAL_SCREEN_COLOR)

    pygame.display.update()
