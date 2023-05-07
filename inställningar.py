import pygame
LEVEL_MAP = [
'                            ',
'                            ',
'        o             o     ',
'       XXXX           XX    ',
'   P                      G ',
'ggggg         gg         XX ',
' XXXX       gg         o    ',
' XX    g  ggXX    gg  gg    ',
'       X  XXXXo   XX  XXX   ',
'o   gggX  XXXXXX  XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXX  ']

TILE_SIZE = 64
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# colors
BG_COLOR = pygame.image.load("bgpic.png")
PLAYER_COLOR = pygame.image.load("spelaren.png")
TILE_COLOR = pygame.image.load("stonetile.png")
Goal_image = pygame.image.load("flagga.png")
coin_image = pygame.image.load("coinn.png")
TILEGRASS_COLOR = pygame.image.load("grasstile.png")

# camera
CAMERA_BORDERS = {
	'left': 100,
	'right': 200,
	'top':100,
	'bottom': 150
}