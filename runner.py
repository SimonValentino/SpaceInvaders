import pygame


pygame.init()


pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(pygame.image.load("space_invaders_icon.png"))
screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)


run_game = True
while run_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
