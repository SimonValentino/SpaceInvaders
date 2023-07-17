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

    def in_bounds(self):
        return self.in_left_bound() and self.in_right_bound()

    def in_left_bound(self):
        return self.x >= consts.LEFT_BOUND

    def in_right_bound(self):
        return self.x <= consts.RIGHT_BOUND


class Alien(_Entity):
    def __init__(self, img_states, coordinates):
        super().__init__(img_states, coordinates)
        self.__direction = 1

    def move(self):
        self.x += consts.ALIEN_SPEED * self.__direction
        self._curr_img_index += 1

    def drop_row(self):
        self.y += consts.ALIEN_VERTICAL_GAP
        self.__direction *= -1


class Defender(_Entity):
    def __init__(self, img_states, coordinates):
        super().__init__(img_states, coordinates)

    def move_right(self):
        if self.in_right_bound():
            self.x += consts.PLAYER_SPEED

    def move_left(self):
        if self.in_left_bound():
            self.x -= consts.PLAYER_SPEED
