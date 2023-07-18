import pygame

import constants as consts


class _Entity:
    def __init__(self, img_states, coordinates):
        if not isinstance(img_states, list):
            img_states = [img_states]
        self._curr_img_index = 0
        self.__img_states = img_states
        self.__num_img_states = len(img_states)
        self.x, self.y = coordinates

    def display(self, screen):
        screen.blit(self.__img_states[self._curr_img_index % self.__num_img_states],
                    (self.x, self.y))
        # Display hitbox
        # pygame.draw.rect(screen, (255, 0, 0), self._body)

    def in_bounds(self):
        return self.in_left_bound() and self.in_right_bound()

    def in_left_bound(self):
        return self.x > consts.LEFT_BOUND

    def in_right_bound(self):
        return self.x < consts.RIGHT_BOUND


class Alien(_Entity):
    def __init__(self, img_states, coordinates):
        super().__init__(img_states, coordinates)
        self.__direction = 1
        self._body = pygame.Rect(self.x + consts.ALIEN_BODY_LEFT_PAD, self.y + consts.ALIEN_BODY_TOP_PAD,
                                 consts.ALIEN_WIDTH, consts.ALIEN_HEIGHT)

    def move(self):
        self.x += consts.ALIEN_SPEED * self.__direction
        self._body.topleft = (self.x + consts.ALIEN_BODY_LEFT_PAD, self.y + consts.ALIEN_BODY_TOP_PAD)
        self._curr_img_index += 1

    def drop_row(self):
        self.y += consts.ALIEN_VERTICAL_GAP
        self._body.topleft = (self.x + consts.ALIEN_BODY_LEFT_PAD, self.y + consts.ALIEN_BODY_TOP_PAD)
        self.__direction *= -1


class Player(_Entity):
    def __init__(self, img_states, coordinates):
        super().__init__(img_states, coordinates)
        self._body = pygame.Rect(self.x + consts.PLAYER_BODY_LEFT_PAD, self.y + consts.PLAYER_BODY_TOP_PAD,
                                 consts.PLAYER_WIDTH, consts.PLAYER_HEIGHT)

    def move_right(self):
        if self.in_right_bound():
            self.x += consts.PLAYER_SPEED
            self._body.topleft = (self.x + consts.PLAYER_BODY_LEFT_PAD, self.y + consts.PLAYER_BODY_TOP_PAD)

    def move_left(self):
        if self.in_left_bound():
            self.x -= consts.PLAYER_SPEED
            self._body.topleft = (self.x + consts.PLAYER_BODY_LEFT_PAD, self.y + consts.PLAYER_BODY_TOP_PAD)


class Bullet(_Entity):
    def __init__(self, img, coordinates):
        super().__init__(img, coordinates)
        self._body = pygame.Rect(self.x + consts.BULLET_BODY_LEFT_PAD, self.y + consts.BULLET_BODY_TOP_PAD,
                                 consts.BULLET_WIDTH, consts.BULLET_HEIGHT)
        self.is_active = False

    def fire(self, coordinates):
        self.x, self.y = coordinates
        self.is_active = True
        self._body.topleft = (self.x + consts.BULLET_BODY_LEFT_PAD, self.y + consts.BULLET_BODY_TOP_PAD)

    def move(self):
        if self.is_active:
            self.y -= consts.BULLET_SPEED
            self._body.topleft = (self.x + consts.BULLET_BODY_LEFT_PAD, self.y + consts.BULLET_BODY_TOP_PAD)

    def in_bounds(self):
        return self.y > consts.TOP_BOUND

    def collides_with(self, entity):
        if self.is_active:
            return self._body.colliderect(entity._body)
        return False
