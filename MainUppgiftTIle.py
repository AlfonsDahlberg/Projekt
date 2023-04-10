#importerar nödvändiga moduler och all nödvändig kod.
import pygame, sys
from inställningar import *
from LEVEL import Level

#pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("PythonSpel")

LEVEL = Level()

#loop för händelser.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #lägger till en "quit" shortcut på "ESC"
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
    screen.blit(BG_COLOR, (0, 0))
    LEVEL.run()

    # ritar logic
    pygame.display.update()
    clock.tick(60)


