import pygame as pg

# visualização
VISUALIZATIONS = False
SHOW_COMRADES = False
SHOW_TARGETS = False
SHOW_HITBOXES = False
SHOW_ROOT_PATH = False

APPEND_COUNTDOWN = 5


DISP_W = 900
DISP_H = 650
BOTTOM_CENTER = (450,650)
DISP_CENTER = (DISP_W/2, DISP_H/2)


# criação do display
display = pg.display.set_mode((DISP_W,DISP_H))
display_rect = display.get_rect()
pg.display.set_caption('Bubbles 2.0')
clock = pg.time.Clock()

# cor
BLACK = (0, 0, 0 )
LIGHT_GRAY = (122, 122, 122)
DARK_GRAY = (60,60,60)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
VIOLET = (127, 0, 255)

# Cores balão
BUBBLE_COLORS = [RED,YELLOW,GREEN,BLUE,VIOLET,ORANGE]
BG_COLOR = 'No color'

AIM_LENGTH = 200

ANGLE_MAX = 180 - 15
ANGLE_MIN = 15

# Movementos Balões Constantes  
BUBBLE_VEL = 15
BUBBLE_RADIUS = 15

GRID_COLS = 20
GRID_ROWS = 10
GAMEOVER_ROWS = 20


HITBOX_SIZE = (BUBBLE_RADIUS * 2) - 4

WALL_WIDTH = 120
FLOOR_HEIGHT = DISP_H - (2 * BUBBLE_RADIUS * (GAMEOVER_ROWS - 1))
ROOM_WIDTH = DISP_W - (2 * WALL_WIDTH)
WALL_BOUND_L = WALL_WIDTH
WALL_BOUND_R = DISP_W - WALL_WIDTH
WALL_BOUND_FLOOR = DISP_H - FLOOR_HEIGHT


URL = "http://localhost:5000/incluir/Jogador"