import pygame.font
from constants import *


class Hud:
    def __init__(self):
        self.__score = 0
        self.__level = 1
        self.__num_lives = 3
        self.__font = pygame.font.Font("assets/press_start_2p.ttf", FONT_SIZE)

    def display(self, screen):
        score_text = self.__font.render("SCORE", True, (255, 255, 255))
        score_value = self.__font.render(str(self.__score), True, (255, 255, 255))
        level_text = self.__font.render("LEVEL", True, (255, 255, 255))
        level_value = self.__font.render(str(self.__level), True, (255, 255, 255))
        num_lives_text = self.__font.render("LIVES", True, (255, 255, 255))
        num_lives_value = self.__font.render(str(self.__num_lives), True, (255, 255, 255))

        screen.blit(score_text, SCORE_TEXT_COORDINATES)
        screen.blit(score_value, SCORE_VALUE_COORDINATES)
        screen.blit(level_text, LEVEL_TEXT_COORDINATES)
        screen.blit(level_value, LEVEL_VALUE_COORDINATES)
        screen.blit(num_lives_text, NUM_LIVES_TEXT_COORDINATES)
        screen.blit(num_lives_value, NUM_LIVES_VALUE_COORDINATES)

    def update_score(self, points):
        self.__score += points

    def next_level(self):
        self.__level += 1

    def loose_life(self):
        self.__num_lives -= 1
