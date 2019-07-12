import pygame 
from Classes import COLORS
from Classes import CONSTANTS
from Classes.Square import *

class MSquare(Square):

	"""static variables"""
	
	def __init__(self):
		super().__init__()
		
		self.dx = 1#pixel units
		self.dy = 1#pixel units
		
		self.xshift = 0
		self.yshift = 0
		self.moving = False
		
		
	def __repr__(self):
			return 'dx: {},  dy: {}'.format(self.x, self.y)

	#def __str__(self):

	#uses a simple rect and an optional transparecncy to display itself to screen
	def display(self, screen):
		pixel_x = self.base_x + (self.x*self.width) + self.xshift
		pixel_y = self.base_y + (self.y*self.width) + self.yshift
		
		pygame.draw.rect(screen,self.color,[pixel_x,pixel_y,self.width,self.width],0)
		if self.mask:
			screen.blit(self.mask_image, [pixel_x, pixel_y])

	#uses self.image only
	def displayImage(self, screen):
		pixel_x = self.base_x + (self.x*self.width) + self.xshift
		pixel_y = self.base_y + (self.y*self.width) + self.yshift
		screen.blit(self.image, [pixel_x, pixel_y])
	
	def slideRight(self):
		self.dx = 2
		self.dy = 0
		self.moving = True
		
	def slideLeft(self):
		self.dx = -2
		self.dy = 0
		self.moving = True
		
	def slideUp(self):
		self.dx = 0
		self.dy = -2
		self.moving = True
		
	def slideDown(self):
		self.dx = 0
		self.dy = +5
		self.moving = True
		
	def update(self):
		if self.moving:
			self.xshift += self.dx
			self.yshift += self.dy
			if abs(self.xshift) >= self.width or abs(self.yshift) >= self.width:
				self.xshift = 0
				self.yshift  = 0
				self.moving  = False
				self.updatePositionAfterSlide()
				
				
	def updatePositionAfterSlide(self):
		if self.dx >=1:
			self.x +=1
		if self.dx <0:
			self.x -= 1
			
		if self.dy >=1:
			self.y +=1
		if self.dy < 0:
			self.y -= 1