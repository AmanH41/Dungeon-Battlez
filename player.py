import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,obstacle_sprites):        
        super().__init__(groups)

        self.image = pygame.image.load('character1/tile000.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2()

        self.obstacle_sprites = obstacle_sprites

    

    def input(self):
        #get potential keys being pressed
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_d]:
            self.direction.x = -1
        elif keys[pygame.K_a]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def update(self):
       self.input()

        
