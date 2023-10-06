import pygame 
from settings import *
from tile import Tile
from player import Player
from debug import debug
from importCSV import *
from random import choice

class Level:
	def __init__(self):

		# get the display surface 
		self.display_surface = pygame.display.get_surface()

		# sprite group setup
		self.visible_sprites = YSortCameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()

		# sprite setup
		self.create_map()

	#this method creats all spirtes 
	def create_map(self):
		layouts = {
			'boundary': import_csv_layout('Assets/DungeonCVS/Dungeon_Boundaryblocks.csv'),
			'entities': import_csv_layout('Assets/DungeonCVS/Dungeon_entities.csv'),
			'objects' : import_csv_layout('Assets\DungeonCVS\Dungeon_objects.csv')
		}

		graphics = {
			'objects': import_folder('Assets\Assets64\objects')
		}

		for style, layout in layouts.items():
				for row_index,row in enumerate(layout):
					for col_index, col in enumerate(row):
						if col != '-1':
							x = col_index * TILESIZE
							y = row_index * TILESIZE
							
							if style == 'boundary':
								Tile((x,y),[self.obstacle_sprites],'invisible')

							if style == 'objects':
								surf = graphics['objects'][int(col)]
								Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'object',surf)

							if style == 'entities':
								if col == '0':
									self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites)
								else:
									pass

	def run(self):
		# update and draw the game
		self.visible_sprites.custom_draw(self.player)
		self.visible_sprites.update()

		debug(self.player.status)  #show player direction 

#this class is for camera and drawing the sprites
class YSortCameraGroup(pygame.sprite.Group):
	def __init__(self):

		super().__init__()
		self.display_surface = pygame.display.get_surface()
		#offset for camera placement 
		self.half_width = self.display_surface.get_size()[0] // 2 	
		self.half_height = self.display_surface.get_size()[1] // 2 		
		self.offset = pygame.math.Vector2()
		
		#creating the floor 
		self.floor_surf = pygame.image.load('Tilemap/DungeonMap.png').convert()
		self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))


	#apply the offset based on player pos so camera centers on player
	def custom_draw(self, player):		

		#getting offset from player
		self.offset.x = player.rect.centerx - self.half_width
		self.offset.y = player.rect.centery - self.half_height	

		#drawing the floor 
		floor_offset_pos = self.floor_rect.topleft - self.offset	
		self.display_surface.blit(self.floor_surf, floor_offset_pos)

		#for sprite in self.sprites():
		for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image, offset_pos)		