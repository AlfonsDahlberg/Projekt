import pygame
from inställningar import *
from support import import_folder
from tile import Goal


class Player(pygame.sprite.Sprite):
	def __init__(self,pos,groups,collision_sprites):
		super().__init__(groups)
		self.touchedGoal = False
		self.animations = None
		self.import_character_assets()
		self.frame_index = 0
		self.animation_speed = 0.15
		self.image = pygame.Surface((TILE_SIZE // 2,TILE_SIZE))
		self.image = PLAYER_COLOR #animations['idle'][self.frame_index]
		self.rect = self.image.get_rect(topleft = pos)
		#spelarens rörelse/hastighet
		self.direction = pygame.math.Vector2()
		self.speed = 8
		self.gravity = 0.8
		self.jump_speed = 16
		self.collision_sprites = collision_sprites
		self.on_floor = False

	def import_character_assets(self):
		#filsökväg för animationer
		character_path = '../graphics/character'
		self.animations = {'idle':[],'run':[],'jump':[],'fall':[]}

		for animation in self.animations.keys():
			full_path = character_path + '/' + animation + '/'
			self.animations[animation] = import_folder(full_path)


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

	def horizontal_collisions(self):
		for sprite in self.collision_sprites.sprites():
			if type(sprite) is Goal:
				if sprite.rect.colliderect(self.rect):
					self.touchedGoal = True
			if sprite.rect.colliderect(self.rect):
				if self.direction.x < 0:
					self.rect.left = sprite.rect.right
				if self.direction.x > 0:
					self.rect.right = sprite.rect.left

	def vertical_collisions(self):
		for sprite in self.collision_sprites.sprites():
			if type(sprite) is Goal:
				if sprite.rect.colliderect(self.rect):
					self.touchedGoal = True
			if sprite.rect.colliderect(self.rect):
				if self.direction.y > 0:
					self.rect.bottom = sprite.rect.top
					self.direction.y = 0
					self.on_floor = True
				if self.direction.y < 0:
					self.rect.top = sprite.rect.bottom
					self.direction.y = 0
		if self.on_floor and self.direction.y != 0:
			self.on_floor = False

	def apply_gravity(self):
		self.direction.y += self.gravity
		self.rect.y += self.direction.y

	def update(self):
		self.input()
		self.rect.x += self.direction.x * self.speed
		self.horizontal_collisions()
		self.apply_gravity()
		self.vertical_collisions()


