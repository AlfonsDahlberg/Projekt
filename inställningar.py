import pygame
LEVEL_MAP = [
'                            ',
'                            ',
'       o              o     ',
'       XXXX           XX    ',
'   P         o              ',
'XXXXX         XX         XX ',
' XXXX       XX       o      ',
' XX    X  XXXX    XX  XX    ',
'   o   X  XXXX    XX  XXX   ',
'    XXXX  XXXXXX  XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXX  ']

TILE_SIZE = 64
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# colors
BG_COLOR = pygame.image.load("bgpic.png")
PLAYER_COLOR = pygame.image.load("spelaren.png")
TILE_COLOR = pygame.image.load("bricktile.png")
coin = pygame.image.load("coinn.png")

# camera
CAMERA_BORDERS = {
	'left': 100,
	'right': 200,
	'top':100,
	'bottom': 150
}