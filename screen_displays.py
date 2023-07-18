import pygame.font
import constants as consts


class Hud:
    def __init__(self):
        self.score = 0
        self.num_lives = 3
        self.__font = pygame.font.Font("assets/press_start_2p.ttf", consts.FONT_SIZE)

    def update_score(self, points):
        self.score += points

    def display(self, screen):
        score_text = self.__font.render("SCORE", True, (255, 255, 255))
        score_value = self.__font.render(str(self.score), True, (255, 255, 255))
        num_lives_text = self.__font.render("LIVES", True, (255, 255, 255))
        num_lives_value = self.__font.render(str(self.num_lives), True, (255, 255, 255))

        screen.blit(score_text, consts.SCORE_TEXT_COORDINATES)
        screen.blit(score_value, consts.SCORE_VALUE_COORDINATES)
        screen.blit(num_lives_text, consts.NUM_LIVES_TEXT_COORDINATES)
        screen.blit(num_lives_value, consts.NUM_LIVES_VALUE_COORDINATES)
