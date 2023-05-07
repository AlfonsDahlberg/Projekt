import pygame
from inställningar import *

from tile import Goal, Coin


class Player(pygame.sprite.Sprite): #klass för spelaren
	def __init__(self,pos,groups,collision_sprites):
		super().__init__(groups)
		self.noOfCollectedCoins = 0
		self.touchedGoal = False
		self.animations = None
		self.frame_index = 0
		self.animation_speed = 0.15
		self.image = pygame.Surface((TILE_SIZE // 2,TILE_SIZE))
		self.image = PLAYER_COLOR
		self.rect = self.image.get_rect(topleft = pos)
		#spelarens rörelse/hastighet
		self.direction = pygame.math.Vector2()
		self.speed = 8
		self.gravity = 0.8
		self.jump_speed = 16
		self.collision_sprites = collision_sprites
		self.on_floor = False

     #keybinds för att styra gubben
	def input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_RIGHT]:
			self.direction.x = 1
		elif keys[pygame.K_LEFT]:
			self.direction.x = -1
		else:
			self.direction.x = 0

		if keys[pygame.K_SPACE] and self.on_floor:
			self.direction.y = -self.jump_speed

    #horizontuella collisioner med sprites
	def horizontal_collisions(self):
		for sprite in self.collision_sprites.sprites():
			if sprite.rect.colliderect(self.rect):
				if type(sprite) is Coin:
					self.noOfCollectedCoins += 1
					sprite.kill()
				if type(sprite) is Goal:
					self.touchedGoal = True
				if self.direction.x < 0:
					self.rect.left = sprite.rect.right
				if self.direction.x > 0:
					self.rect.right = sprite.rect.left

    #vertikala kollisioner med sprites
	def vertical_collisions(self):
		for sprite in self.collision_sprites.sprites():
			if sprite.rect.colliderect(self.rect):
				if type(sprite) is Coin:
					self.noOfCollectedCoins += 1
					sprite.kill()
				if type(sprite) is Goal:
					self.touchedGoal = True
				if self.direction.y > 0:
					self.rect.bottom = sprite.rect.top
					self.direction.y = 0
					self.on_floor = True
				if self.direction.y < 0:
					self.rect.top = sprite.rect.bottom
					self.direction.y = 0
		if self.on_floor and self.direction.y != 0:
			self.on_floor = False

    #funktion för hur gravitation påverkar spelaren
	def apply_gravity(self):
		self.direction.y += self.gravity
		self.rect.y += self.direction.y

	#uppdaterar spelaren i varje loop
	def update(self):
		self.input()
		self.rect.x += self.direction.x * self.speed
		self.horizontal_collisions()
		self.apply_gravity()
		self.vertical_collisions()


