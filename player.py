import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,obstacle_sprites):        
        super().__init__(groups)

        self.image = pygame.image.load('character1/16xwalking/tile000.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (64,64))
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -24)

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

        self.hitbox.x += self.direction.x * speed
        self.collsion('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collsion('vertical')
        self.rect.center = self.hitbox.center

    def collsion(self,direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left #if player is moving to the right 
                    if self.direction.x < 0 :
                        self.hitbox.left = sprite.hitbox.right # if palyer is moving to the left 

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: # moving down on a object 
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: # moving up on a object
                        self.hitbox.top = sprite.hitbox.bottom

    

    def update(self):
       self.input()
       self.move(self.speed)



        