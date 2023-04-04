import pygame
from pygame.locals import *

pygame.init()

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Platformer")

# Load images
background_img = pygame.image.load("gymbild.jpg")
platform_img = pygame.image.load("pixil-frame-0.png")
player_img = pygame.image.load("result.png")
enemy_img = pygame.image.load("pixilart-drawing.png")

# Define player class
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.speed = 5
        self.jump_height = 20
        self.gravity = 1
        self.is_jumping = False
        self.image = player_img

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.jump_speed = self.jump_height

    def update(self, obstacles, enemies):
        if self.is_jumping:
            self.y -= self.jump_speed
            self.jump_speed -= self.gravity
            if self.jump_speed <= 0:
                self.is_jumping = False
        else:
            self.y += self.gravity
        self.check_collisions(obstacles, enemies)

    def check_collisions(self, obstacles, enemies):
        for obstacle in obstacles:
            if self.x + self.width > obstacle.x and self.x < obstacle.x + obstacle.width:
                if self.y + self.height > obstacle.y and self.y < obstacle.y + obstacle.height:
                    # Collision detected
                    self.reset_position()
        for enemy in enemies:
            if self.x + self.width > enemy.x and self.x < enemy.x + enemy.width:
                if self.y + self.height > enemy.y and self.y < enemy.y + enemy.height:
                    # Collision detected
                    self.reset_position()

    def reset_position(self):
        self.x = 100
        self.y = 100

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

# Define obstacle class
class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.image = platform_img

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

# Define enemy class
class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.speed = 3
        self.image = enemy_img

    def update(self):
        self.x += self.speed

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

# Create player, obstacles, and enemies
player = Player(100, 100)
obstacles = [Obstacle(100, 250), Obstacle(300, 400)]
enemies = [Enemy(500, 300), Enemy(700, 500)]

# Main game loop
run = True
while run:

    # Draw background, obstacles, and enemies
    screen.blit(background_img, (0,0))
    for obstacle in obstacles:
        obstacle.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)
    # Update player and enemies
    player.update(obstacles, enemies)
    for enemy in enemies:
        enemy.update()

    # Draw player and enemies
    player.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)

    # Check for user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move_left()
    if keys[pygame.K_RIGHT]:
        player.move_right()
    if keys[pygame.K_SPACE]:
        player.jump()

    # Check for quit event or quit button press
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False

    # Update display
    pygame.display.update()

# Quit game
pygame.quit()


