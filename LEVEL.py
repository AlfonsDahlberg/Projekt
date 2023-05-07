import pygame
from inställningar import *
from tile import Tile, Goal, Coin, Score, TileGrass
from player import Player
screen = (1280, 720)

class Level:
    def __init__(self):
        #nivå setup
        self.display_surface = pygame.display.get_surface()
        #sprite groups
        self.collision_sprites = pygame.sprite.Group()
        self.visible_sprites = CameraGroup()
        self.active_sprites = pygame.sprite.Group()

        self.setup_LEVEL()

    def setup_LEVEL(self):
        for row_index,row in enumerate(LEVEL_MAP):
            for col_index,col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if col == 'X':
                    Tile((x,y), [self.visible_sprites,self.collision_sprites])
                if col == 'P':
                    self.player = Player((x, y), [self.visible_sprites, self.active_sprites], self.collision_sprites)
                if col == 'G':
                    Goal((x,y), [self.visible_sprites,self.collision_sprites])
                if col == 'o':
                    Coin((x,y), [self.visible_sprites,self.collision_sprites])
                if col == 'g':
                    TileGrass((x,y), [self.visible_sprites,self.collision_sprites])


    def reset_level(self):
        # rensa sprite-grupperna och skapa nya instanser av spelaren och plattformar
        self.__init__()

    def run(self):
        #kör spelet(leveln)
        self.active_sprites.update()
        self.visible_sprites.costum_draw(self.player)

    def isPlayerDead(self):
        return self.player.rect.bottom > 1000

    def isPlayerInGoal(self):
        return self.player.touchedGoal

    def noOfCoinsPickedUp(self):
        return self.player.noOfCollectedCoins


class CameraGroup(pygame.sprite.Group): #klass för kameran som följer spelaren.
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2(100,300)

        #camera inte centrerad
        cam_left = CAMERA_BORDERS["left"]
        cam_top = CAMERA_BORDERS["top"]
        cam_width = self.display_surface.get_size()[0] - (cam_left+ CAMERA_BORDERS["right"])
        cam_height = self.display_surface.get_size()[1] - (cam_top + CAMERA_BORDERS["bottom"])

        self.camera_rect = pygame.Rect(cam_left,cam_top,cam_width,cam_height)

    def costum_draw(self,player):
        #får kamera positionen
        if player.rect.left < self.camera_rect.left:
            self.camera_rect.left = player.rect.left
        if player.rect.right > self.camera_rect.right:
            self.camera_rect.right = player.rect.right
        if player.rect.top < self.camera_rect.top:
            self.camera_rect.top = player.rect.top
        if player.rect.bottom > self.camera_rect.bottom:
            self.camera_rect.bottom = player.rect.bottom

        #camera offset
        self.offset = pygame.math.Vector2(
            self.camera_rect.left - CAMERA_BORDERS["left"],
            self.camera_rect.top - CAMERA_BORDERS["top"])

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)

    