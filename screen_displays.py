import pygame.font
from constants import *


class Hud:
    def __init__(self):
        self.score = 0
        self.__level = 1
        self.num_lives = 3
        self.__font = pygame.font.Font("assets/press_start_2p.ttf", FONT_SIZE)

    def display(self, screen):
        score_text = self.__font.render("SCORE", True, (255, 255, 255))
        score_value = self.__font.render(str(self.score), True, (255, 255, 255))
        level_text = self.__font.render("LEVEL", True, (255, 255, 255))
        level_value = self.__font.render(str(self.__level), True, (255, 255, 255))
        num_lives_text = self.__font.render("LIVES", True, (255, 255, 255))
        num_lives_value = self.__font.render(str(self.num_lives), True, (255, 255, 255))

        screen.blit(score_text, SCORE_TEXT_COORDINATES)
        screen.blit(score_value, SCORE_VALUE_COORDINATES)
        screen.blit(level_text, LEVEL_TEXT_COORDINATES)
        screen.blit(level_value, LEVEL_VALUE_COORDINATES)
        screen.blit(num_lives_text, NUM_LIVES_TEXT_COORDINATES)
        screen.blit(num_lives_value, NUM_LIVES_VALUE_COORDINATES)

    def next_level(self):
        self.__level += 1


def game_over_screen(screen, hud):
    font = pygame.font.Font("assets/press_start_2p.ttf", FONT_SIZE)

    game_over_text = font.render("GAME OVER", True, (255, 255, 255))
    game_over_score_text = font.render(f"SCORE: {hud.score}", True, (255, 255, 255))
    restart_text = font.render("R TO RESTART", True, (255, 255, 255))

    score = hud.score
    num_digits_in_score = 1 if score == 0 else 0
    while score != 0:
        score //= 10
        num_digits_in_score += 1

    screen.blit(game_over_text, GAME_OVER_TEXT_COORDINATES)
    screen.blit(game_over_score_text,
                (SCREEN_SIZE[0] / 2 - FONT_SIZE * (7 + num_digits_in_score) / 2,
                 GAME_OVER_SCORE_TEXT_Y_COORDINATE))
    screen.blit(restart_text, RESTART_TEXT_COORDINATES)
