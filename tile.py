import pygame
from inställningar import *

class Tile(pygame.sprite.Sprite):
	def __init__(self,pos,groups,):
		super().__init__(groups)
		self.image = pygame.Surface((TILE_SIZE,TILE_SIZE))
		self.image = TILE_COLOR
		self.rect = self.image.get_rect(topleft = pos)