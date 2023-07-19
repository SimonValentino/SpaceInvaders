import pygame
from constants import *


class _Entity:
    def __init__(self, img_states, death_states, coordinates):
        if not isinstance(img_states, list):
            img_states = [img_states]
        self.__img_states = img_states
        self._img_frame = 0
        self.__num_img_states = len(img_states)

        if not isinstance(death_states, list):
            death_states = [death_states]
        self.__death_states = death_states
        self.__death_frame = 0
        self.__is_dead = False
        self.set_to_remove = False

        self.x, self.y = coordinates

    def display(self, screen):
        if self.__is_dead:
            if self.__death_frame < len(self.__death_states):
                screen.blit(self.__death_states[self.__death_frame],
                            (self.x, self.y))
                self.__death_frame += 1
            else:
                self.set_to_remove = True
        else:
            screen.blit(self.__img_states[self._img_frame % self.__num_img_states],
                        (self.x, self.y))

        # Display hitbox
        # pygame.draw.rect(screen, (255, 0, 0), self._body)

    def in_bounds(self):
        return self.in_left_bound() and self.in_right_bound()

    def in_left_bound(self):
        return self.x > LEFT_BOUND

    def in_right_bound(self):
        return self.x < RIGHT_BOUND

    def kill(self):
        self.__is_dead = True


class Alien(_Entity):
    def __init__(self, img_states, coordinates):
        death_states = [
            pygame.image.load("assets/icons/alien_death_state1.png"),
            pygame.image.load("assets/icons/alien_death_state2.png"),
            pygame.image.load("assets/icons/alien_death_state3.png")
        ]
        super().__init__(img_states, death_states, coordinates)
        self.__direction = 1
        self._body = pygame.Rect(self.x + ALIEN_BODY_LEFT_PAD, self.y + ALIEN_BODY_TOP_PAD,
                                 ALIEN_WIDTH, ALIEN_HEIGHT)

    def move(self):
        self.x += ALIEN_SPEED * self.__direction
        self._body.topleft = (self.x + ALIEN_BODY_LEFT_PAD, self.y + ALIEN_BODY_TOP_PAD)
        self._img_frame += 1

    def drop_row(self):
        self.y += ALIEN_VERTICAL_GAP
        self._body.topleft = (self.x + ALIEN_BODY_LEFT_PAD, self.y + ALIEN_BODY_TOP_PAD)
        self.__direction *= -1


class Player(_Entity):
    def __init__(self, img_states, coordinates):
        death_states = [
                           pygame.image.load("assets/icons/player_death.png")
                       ] * 100
        super().__init__(img_states, death_states, coordinates)
        self._body = pygame.Rect(self.x + PLAYER_BODY_LEFT_PAD, self.y + PLAYER_BODY_TOP_PAD,
                                 PLAYER_WIDTH, PLAYER_HEIGHT)

    def move_right(self):
        if self.in_right_bound():
            self.x += PLAYER_SPEED
            self._body.topleft = (self.x + PLAYER_BODY_LEFT_PAD, self.y + PLAYER_BODY_TOP_PAD)

    def move_left(self):
        if self.in_left_bound():
            self.x -= PLAYER_SPEED
            self._body.topleft = (self.x + PLAYER_BODY_LEFT_PAD, self.y + PLAYER_BODY_TOP_PAD)


class _Bullet(_Entity):
    def __init__(self, img_states, death_states, coordinates):
        super().__init__(img_states, death_states, coordinates)
        self._body = pygame.Rect(self.x + BULLET_BODY_LEFT_PAD, self.y + BULLET_BODY_TOP_PAD,
                                 BULLET_WIDTH, BULLET_HEIGHT)

    def collides_with(self, entity):
        return self._body.colliderect(entity._body)

    def fire(self, coordinates):
        self.x, self.y = coordinates
        self._body.topleft = (self.x + BULLET_BODY_LEFT_PAD, self.y + BULLET_BODY_TOP_PAD)


class PlayerBullet(_Bullet):
    def __init__(self, img_states, coordinates):
        super().__init__(img_states, None, coordinates)
        self.__speed = PLAYER_BULLET_SPEED
        self.is_active = False

    def move(self):
        if self.is_active:
            self.y -= self.__speed
            self._body.topleft = (self.x + BULLET_BODY_LEFT_PAD, self.y + BULLET_BODY_TOP_PAD)

    def in_bounds(self):
        return self.y > TOP_BOUND

    def fire(self, coordinates):
        super().fire(coordinates)
        self.is_active = True

    def collides_with(self, entity):
        if self.is_active:
            return super().collides_with(entity)


class AlienBullet(_Bullet):
    def __init__(self, img_states, coordinates):
        super().__init__(img_states, None, coordinates)
        self.__speed = BASE_ALIEN_BULLET_SPEED

    def move(self):
        self.y += self.__speed
        self._body.topleft = (self.x + BULLET_BODY_LEFT_PAD, self.y + BULLET_BODY_TOP_PAD)

    def in_bounds(self):
        return self.y < BOTTOM_BOUND
