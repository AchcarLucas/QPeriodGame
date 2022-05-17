import pygame

class GameFont(object):
    def initFont():
        pygame.font.init()

        if(GameFont.comic_san_30 == None):
            GameFont.comic_san_30 = pygame.font.SysFont('Comic Sans MS', 30)

        if(GameFont.arial_12 == None):
            GameFont.arial_12 = pygame.font.SysFont('Arial', 12)

        if(GameFont.arial_30 == None):
            GameFont.arial_30 = pygame.font.SysFont('Arial', 30)

GameFont.comic_san_30 = None
GameFont.arial_30 = None
GameFont.arial_12 = None

