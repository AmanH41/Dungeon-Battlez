import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __iniit__(self, pos, groups):
        super().__init__(groups)