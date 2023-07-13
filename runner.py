import pygame


pygame.init()

screen = pygame.display.set_mode((800, 800))

run_game = True
while run_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
