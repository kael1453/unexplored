"""
This is where all the constants are stored.

Import this as 'c' for consistency.
"""

# Constants.
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_TITLE = 'Unexplored'
WORLD_BOTTOM = -200

# Constants used to scale our sprites from their original size.
PIXEL_SCALING = 4
INTRO_SCALING = 3
UI_SCALING = 4
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = 32

# Size of the map
MAP_WIDTH = 256 * PIXEL_SCALING
MAP_HEIGHT = 256 * PIXEL_SCALING

# Used for culling bullet sprites beyond a certain distance from the player, in pixels.
CULL_DISTANCE_X = 4000
CULL_DISTANCE_Y = 2000

# Movement speed of player, in pixels per frame.
PLAYER_WALK_SPEED = 4.6
PLAYER_RUN_SPEED = 10.3
GRAVITY = 0.95
PLAYER_JUMP_SPEED = 28
UPDATES_PER_FRAME = 10
EFFECT_UPDATES_PER_FRAME = 5

# Cinematic intro constants.
INTRO_UPDATES_PER_FRAME = 10

# Updates for the gun shooting animation.
GUN_UPDATES_PER_FRAME = 4

# How many pixels to keep as a minimum margin between
# the character and the edge of the screen.
LEFT_VIEWPORT_MARGIN = SCREEN_WIDTH // 2 + 50
RIGHT_VIEWPORT_MARGIN = SCREEN_WIDTH // 2 - 50
BOTTOM_VIEWPORT_MARGIN = SCREEN_HEIGHT // 2 - 100
TOP_VIEWPORT_MARGIN = SCREEN_HEIGHT // 2 + 100

PLAYER_START_X = 250
PLAYER_START_Y = 2000

# Constants used to track if the player is facing left or right.
RIGHT_FACING = 0
LEFT_FACING = 1

# Bullet speed, in pixels per frame.
BULLET_SPEED = 55

# Precalculated random numbers, used instead of random() for performance.
RANDOM_NUMBERS_8 = []
