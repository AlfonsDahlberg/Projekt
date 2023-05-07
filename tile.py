import pygame
import self

from inställningar import *

#Klass för marken
class Tile(pygame.sprite.Sprite):
	def __init__(self,pos,groups,):
		super().__init__(groups)
		self.image = pygame.Surface((TILE_SIZE,TILE_SIZE))
		self.image = TILE_COLOR
		self.rect = self.image.get_rect(topleft = pos)

#Klass för marken
class TileGrass(pygame.sprite.Sprite):
	def __init__(self,pos,groups,):
		super().__init__(groups)
		self.image = pygame.Surface((TILE_SIZE,TILE_SIZE))
		self.image = TILEGRASS_COLOR
		self.rect = self.image.get_rect(topleft = pos)

#Klass för målet
class Goal(pygame.sprite.Sprite):
	def __init__(self,pos,groups,):
		super().__init__(groups)
		self.image = pygame.Surface((20,70))
		self.image = Goal_image
		self.rect = self.image.get_rect(topleft = pos)

#Klass för coins
class Coin(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		self.image = pygame.Surface((32,32))
		self.image = coin_image
		self.rect = self.image.get_rect(topleft = pos)

#Klass för score
class Score():
	def __init__(self, pos, text_input, font):
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color = "White"
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		screen.blit(self.text, self.text_rect)

