import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,obstacle_sprites):        
        super().__init__(groups)

        self.image = pygame.image.load('character1/16xwalking/tile000.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (64,64))
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2()

        self.obstacle_sprites = obstacle_sprites
        self.speed = 5
    

    def input(self):
        #get keys being pressed
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0
    
    def move(self, speed):
        #if vector is not != 0 
        if self.direction.magnitude() != 0:
            #normalize the speed of diagonal movements 
            self.direction = self.direction.normalize()

        self.rect.x += self.direction.x * speed
        self.collsion('horizontal')
        self.rect.y += self.direction.y * speed
        self.collsion('vertical')
 

    def collsion(self,direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left #if player is moving to the right 
                    if self.direction.x < 0 :
                        self.rect.left = sprite.rect.right # if palyer is moving to the left 

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0: # moving down
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0: # moving up 
                        self.rect.top = sprite.rect.bottom

        


    def update(self):
       self.input()
       self.move(self.speed)



        
