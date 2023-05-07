#importerar nödvändiga moduler och all nödvändig kod.
import pygame, sys
from inställningar import *
from LEVEL import Level
from button import Button
from tile import Score

replay = True

#pygame setup
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("PythonSpel")
SCREEN = pygame.display.set_mode((1280, 720))

LEVEL = Level()

BG = pygame.image.load("MAINMENY.jpg")

def get_font(size): #retunerar font i önskad storlek.
    return pygame.font.Font("font.ttf", size)

def play(): # Spel skärmen
    #loop för händelser i spelet.

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos() #får mus positionen.
        SCREEN.blit(BG_COLOR, (0, 0)) #ritar bakrunden
        LEVEL.run()#updaterar alla sprites

        if LEVEL.isPlayerInGoal():
            victoryScreen()

        if LEVEL.isPlayerDead():
            deathScreen()

        SCORE = Score(pos=(100, 100), text_input=str(LEVEL.noOfCoinsPickedUp()), font=get_font(75))
        SCORE.update(SCREEN)

        #Knapp för att lämna spelet
        PLAY_BACK = Button(image=None, pos=(1000, 100),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green") # Väljer färger och storlek för Knapp texten
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def deathScreen(): # En skärm som kommer upp när man dör med knappar "back" och "retry"
    while True:

        DS_MOUSE_POS = pygame.mouse.get_pos()
        #ställer in knapparna
        SCREEN.blit(BG_COLOR, (0, 0))
        DS_TEXT = get_font(100).render("YOU DIED!", True, "#000000")
        DS_RECT = DS_TEXT.get_rect(center=(640, 100))
        BACK_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(640, 550),
                             text_input="BACK", font=get_font(60), base_color="#d7fcd4", hovering_color="Pink")
        RETRY_BUTTON = Button(image=pygame.image.load("Play Rect.png"), pos=(640, 250),
                             text_input="RETRY!", font=get_font(60), base_color="#d7fcd4", hovering_color="Pink")
        SCREEN.blit(DS_TEXT, DS_RECT)

        for button in [RETRY_BUTTON, BACK_BUTTON]:
            button.changeColor(DS_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RETRY_BUTTON.checkForInput(DS_MOUSE_POS):
                    LEVEL.reset_level()
                    play()
                if BACK_BUTTON.checkForInput(DS_MOUSE_POS):
                    main_menu()
        # ritar logic
        pygame.display.update()
        clock.tick(60)

def victoryScreen(): # En skärm som kommer upp när man dör med knappar "back" och "retry"
    while True:

        DS_MOUSE_POS = pygame.mouse.get_pos()
        #ställer in knapparna
        SCREEN.blit(BG_COLOR, (0, 0))
        DS_TEXT = get_font(100).render("Victory!", True, "#000000")
        DS_RECT = DS_TEXT.get_rect(center=(640, 100))
        BACK_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(640, 550),
                             text_input="BACK", font=get_font(60), base_color="#d7fcd4", hovering_color="Pink")
        SCREEN.blit(DS_TEXT, DS_RECT)

        for button in [BACK_BUTTON]:
            button.changeColor(DS_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(DS_MOUSE_POS):
                    main_menu()
        # ritar logic
        pygame.display.update()
        clock.tick(60)



def options(): # Skrämen för eventuella inställningar
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("There are no OPTIONS.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()
        clock.tick(60)


def main_menu(): # Meny skärmen
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#000000")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("Play Rect.png"), pos=(640, 250),
                                 text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="Green")
        OPTIONS_BUTTON = Button(image=pygame.image.load("Options Rect.png"), pos=(640, 400),
                                    text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4",
                                    hovering_color="Green")
        QUIT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(640, 550),
                                 text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="Green")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    LEVEL.reset_level()
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

            # ritar logic
            pygame.display.update()
            clock.tick(60)

main_menu()

