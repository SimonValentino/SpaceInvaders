# Screen constants
SCREEN_SIZE = (800, 1000)
ICON_SIZE = (64, 64)
LEFT_BOUND = 0
RIGHT_BOUND = SCREEN_SIZE[0] - ICON_SIZE[0]
BG_SCREEN_COLOR = (0, 0, 0)  # Black in RGB

# Player constants
INITIAL_PLAYER_COORDINATES = (SCREEN_SIZE[0] / 2 - ICON_SIZE[0] / 2,
                              SCREEN_SIZE[1] / 6 * 5)
PLAYER_SPEED = 5  # Num pixels the player moves left or right with each key pressed

# Alien constants
ALIEN_SPEED = 3
NUM_ALIENS_PER_ROW = 10
NUM_ALIEN_ROWS = 5
ALIEN_VERTICAL_GAP = SCREEN_SIZE[1] / 20

# Used to maintain smooth movement
FPS = 30
