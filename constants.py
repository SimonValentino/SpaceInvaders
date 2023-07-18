# Screen constants
SCREEN_SIZE = (800, 1000)
ICON_SIZE = (64, 64)
LEFT_BOUND = 0
RIGHT_BOUND = SCREEN_SIZE[0] - ICON_SIZE[0]
TOP_BOUND = 0
BG_SCREEN_COLOR = (0, 0, 0)  # Black in RGB

# Player constants
INITIAL_PLAYER_COORDINATES = (SCREEN_SIZE[0] / 2 - ICON_SIZE[0] / 2,
                              SCREEN_SIZE[1] / 6 * 5)
PLAYER_WIDTH = 52
PLAYER_HEIGHT = 31
PLAYER_SPEED = 5  # Num pixels the player moves left or right with each key pressed

# Bullet constants
BULLET_WIDTH = 4
BULLET_HEIGHT = 13
BULLET_SPEED = 30

# Alien constants
INITIAL_ALIEN_COORDINATES = (SCREEN_SIZE[0] / 16, SCREEN_SIZE[1] / 10)
ALIEN_WIDTH = 60
ALIEN_HEIGHT = 40
NUM_ALIENS_PER_ROW = 10
BASE_NUM_ALIEN_ROWS = 3
ALIEN_HORIZONTAL_GAP = (SCREEN_SIZE[0] - 2 * INITIAL_ALIEN_COORDINATES[0] - ICON_SIZE[0]) / (NUM_ALIENS_PER_ROW - 1)
ALIEN_VERTICAL_GAP = SCREEN_SIZE[1] / 20
BASE_ALIEN_MOVES_PER_SECOND = 2
ALIEN_SPEED = 10  # Num pixels alien traverses each time it moves

# Other
FPS = 30  # Used to maintain smooth movement
