import constants as consts


class __Entity:
    def __init__(self, img, coordinates):
        self.img = img
        self.x, self.y = coordinates

    def display(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def in_bounds(self):
        return self.x >= consts.RIGHT_BOUND or self.x <= consts.LEFT_BOUND


class Alien(__Entity):
    def __init__(self, img, coordinates):
        super().__init__(img, coordinates)
        self.__direction = 1

    def move(self):
        self.x += consts.ALIEN_SPEED * self.__direction

    def drop_row(self):
        self.y -= consts.ALIEN_VERTICAL_GAP
        self.__direction *= -1


class Defender(__Entity):
    def __init__(self, img, coordinates):
        super().__init__(img, coordinates)
        self.img = img

    def move_right(self):
        self.x += consts.PLAYER_SPEED

    def move_left(self):
        self.x -= consts.PLAYER_SPEED


