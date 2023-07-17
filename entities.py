import constants as consts


class _Entity:
    def __init__(self, img, coordinates):
        self.img = img
        self.x, self.y = coordinates

    def display(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def in_left_bound(self):
        return self.x >= consts.LEFT_BOUND

    def in_right_bound(self):
        return self.x <= consts.RIGHT_BOUND


class Alien(_Entity):
    def __init__(self, img, coordinates):
        super().__init__(img, coordinates)
        self.__direction = 1

    def move(self):
        self.x += consts.ALIEN_SPEED * self.__direction

    def drop_row(self):
        self.y -= consts.ALIEN_VERTICAL_GAP
        self.__direction *= -1


class Defender(_Entity):
    def __init__(self, img, coordinates):
        super().__init__(img, coordinates)
        self.img = img

    def move_right(self):
        self.x += consts.PLAYER_SPEED

    def move_left(self):
        self.x -= consts.PLAYER_SPEED


