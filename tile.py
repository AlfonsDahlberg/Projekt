import pygame
from inställningar import *

#Klass för marken
class Tile(pygame.sprite.Sprite):
	def __init__(self,pos,groups,):
		super().__init__(groups)
		self.image = pygame.Surface((TILE_SIZE,TILE_SIZE))
		self.image = TILE_COLOR
		self.rect = self.image.get_rect(topleft = pos)

#Klass för målet
class Goal(pygame.sprite.Sprite):
	def __init__(self,pos,groups,):
		super().__init__(groups)
		self.image = pygame.Surface((20,70))
		self.image = Goal_image
		self.rect = self.image.get_rect(topleft = pos)
