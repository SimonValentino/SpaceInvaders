SCREEN_SIZE = (800, 600)
ICON_SIZE = (64, 64)
LEFT_BOUND = 0
RIGHT_BOUND = SCREEN_SIZE[0] - ICON_SIZE[0]

INITIAL_PLAYER_COORDINATES = (SCREEN_SIZE[0] / 2 - ICON_SIZE[0] / 2,
                              SCREEN_SIZE[1] / 6 * 5)

NUM_ALIENS_PER_ROW = 10
ALIEN_START_X = 50
ALIEN_START_Y = 50
ALIEN_HORIZONTAL_GAP = 70
ALIEN_VERTICAL_GAP = 50

# Black in RGB
BG_SCREEN_COLOR = (0, 0, 0)

# Num pixels the player moves left or right with each key pressed
PLAYER_SPEED = 5

# Used to maintain smooth movement
FPS = 30
