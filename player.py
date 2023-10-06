import pygame
from settings import *
from importCSV import import_folder

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,obstacle_sprites):        
        super().__init__(groups)

        self.image = pygame.image.load('Assets/Samurai/down_idle/idle_down.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -24)        #player hitbox from the top and bottom are reduced by 24
        self.obstacle_sprites = obstacle_sprites        #add player to the obtacle_sprites

        
		# graphics setup
        self.import_player_assets()
        self.status = 'down'
        self.frame_index = 1
        self.animation_speed = 0.15
        
        #movments
        self.direction = pygame.math.Vector2()
        self.speed = 6
        self.attacking = False 
        self.attack_cooldown = 400 
        self.attack_time = None
        
    def input(self):
        #get keys being pressed
        keys = pygame.key.get_pressed()
        #directional inputs
        if keys[pygame.K_w]:      
            self.direction.y = -1
            self.status = 'up'
        elif keys[pygame.K_s]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0

        if keys[pygame.K_d]:
            self.direction.x = 1
            self.status = 'right'

        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.status = 'left'
        else:
            self.direction.x = 0

        #attack input 
        if keys[pygame.K_u] and not self.attacking:
            self.attacking = True
            self.attack_time = pygame.time.get_ticks()
            print("attacking")

        #special ability input 
        if keys[pygame.K_i] and not self.attacking:
            self.attacking = True
            self.attack_time = pygame.time.get_ticks()
            print("special move")

        
    def get_status(self):
		# idle status
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status + '_idle'

        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if not 'attack' in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle','_attack')
                else:
                    self.status = self.status + '_attack'
        else:
            if 'attack' in self.status:
                self.status = self.status.replace('_attack','')

    def import_player_assets(self):
        character_path = 'Assets/Samurai/'
        self.animations = {'up': [],'down': [],'left': [],'right': [],
			'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[],
			'right_attack':[],'left_attack':[],'up_attack':[],'down_attack':[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)
        print(self.animations)

    
    def animate(self):
        animation = self.animations[self.status]

		# loop over the frame index 
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

		# set the image
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)
        

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

    def cooldown(self):
        current_time = pygame.time.get_ticks()
        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False
            

    def update(self):
       self.input()
       self.cooldown()
       self.get_status()
       self.animate()
       self.move(self.speed)
       



        
