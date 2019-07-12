import pygame 
from Classes import COLORS
from Classes import CONSTANTS

class Background(object):

	"""static variables"""
	
	def __init__(self, window_size):
	
		self.x = 0#pixel units
		self.y = 0#pixel units
		
		self.screen_width = window_size[0]#pixel units
		self.screen_height = window_size[1]#pixel units
		
		self.image = pygame.image.load("Images/background tile light4.png")
		self.tile_width = CONSTANTS.SQUARE_WIDTH
		self.image = pygame.transform.scale(self.image,(self.tile_width,self.tile_width))



	def display(self, screen):
		
		for x in range(self.x, self.screen_width, self.tile_width ):
			for y in range(self.y, self.screen_height, self.tile_width ):
				screen.blit(self.image, [x,y])
		
	def setPosition(self, pos):
		self.x = pos[0]
		self.y = pos[1]
		