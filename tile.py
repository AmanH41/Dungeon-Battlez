import pygame 
from settings import *

class Tile(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		self.image = pygame.image.load('Assets/test/rock.png').convert_alpha()
		self.image = pygame.transform.scale(self.image,(64,64))
		
		self.rect = self.image.get_rect(topleft = pos)