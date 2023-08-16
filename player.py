import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,obstacle_sprites):        
        super().__init__(groups)

        self.image = pygame.image.load('character1/16xwalking/tile000.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2()

        self.obstacle_sprites = obstacle_sprites
        self.speed = 5
    

    def input(self):
        #get potential keys being pressed
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            self.direction.y = -.5
        elif keys[pygame.K_s]:
            self.direction.y = .5
        else:
            self.direction.y = 0

        if keys[pygame.K_d]:
            self.direction.x = .5
        elif keys[pygame.K_a]:
            self.direction.x = -.5
        else:
            self.direction.x = 0
    
    def move(self, speed):
        #if vector is not != 0 
        if self.direction.magnitude() != 0:
            #normalize the speed of diagonal movements 
            self.direction = self.direction.normalize()
        #speed of all other movements 
        self.rect.center += self.direction * speed 

    def update(self):
       self.input()
       self.move(self.speed)

        
