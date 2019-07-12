import pygame 
from Classes import COLORS
from Classes import CONSTANTS

class Square(object):

	"""static variables"""
	#image = pygame.image.load("Images/Square.png")
	image = pygame.image.load("Images/square_phantom32x32.png")

	#mask_image = pygame.image.load("Images/square_grey32x32.png")
	mask_image = pygame.image.load("Images/square_transparency32x32in.png")
	#mask_image = pygame.image.load("Images/square_phantom32x32.png")
	#mask_image = pygame.image.load("Images/circle_r16.png")

	
	def __init__(self):
		"""position & size"""
		#base = pixel position of the grid it belongs to
		self.base_x = 0#pixel units
		self.base_y = 0#pixel units
		self.x = 1#square units
		self.y = 1#square units
		self.width = CONSTANTS.SQUARE_WIDTH#40#pixel units
		
		"""color & images"""
		self.color = COLORS.BLUE
		#resize image to self.width
		self.image = pygame.transform.scale(Square.image,(self.width,self.width))
		self.mask_image = pygame.transform.scale(Square.mask_image,(self.width,self.width))
		"""display states"""
		self.showColor = True #background color
		self.showImage = True #main image
		self.showMask = True #second image
		
	def __repr__(self):
			return 'x: {},  y: {}, color: {}'.format(self.x, self.y, self.color)

	#def __str__(self):
	
	#uses a simple rect and an optional transparecncy to display itself to screen
	def display(self, screen):
		pixel_x = self.base_x + self.x*self.width
		pixel_y = self.base_y + self.y*self.width
		
		if self.showColor:
			pygame.draw.rect(screen,self.color,[pixel_x,pixel_y,self.width,self.width],0)

		if self.showImage:
			screen.blit(self.image, [pixel_x, pixel_y])

		if self.showMask:
			screen.blit(self.mask_image, [pixel_x, pixel_y])

	#uses self.image only
	def displayImage(self, screen):
		pixel_x = self.base_x + self.x*self.width
		pixel_y = self.base_y + self.y*self.width
		screen.blit(self.image, [pixel_x, pixel_y])
	
	def setBase(self, pos):
		self.base_x = pos[0]
		self.base_y = pos[1]
		
	def setPosition(self, pos):
		self.x = pos[0]
		self.y = pos[1]
	
	""" un-necesary due to use of square units
	def setGridPosition(self, pos):
		self.x = pos[0]*self.width
		self.y = pos[1]*self.width
		"""
	def getPosition(self):
		return (self.x, self.y)
	
		
	def setWidth(self, w):
		self.width = w
	
	def setImage(self, image_name):
		self.image = pygame.image.load(image_name)
		self.image = pygame.transform.scale(self.image,(self.width,self.width))
		
	def setColor(self, c):
		self.color = c

	def setColorOff(self):
		self.showColor = False
		
	def setColorOn(self):
		self.showColor =True
		
	def setImageOff(self):
		self.showImage = False
		
	def setImageOn(self):
		self.showImage = True
		
	def setMaskOff(self):
		self.showMask = False
	
	def setMaskOn(self):
		self.showMask = True
		
	def moveRight(self):
		self.x += 1
	
	def moveLeft(self):
		self.x -= 1
		
	def moveDown(self):
		self.y += 1
		
	def moveUp(self):
		self.y -=1
	
	def copy(self, s):
		#position & size
		self.base_x = s.base_x
		self.base_y = s.base_y
		self.x = s.x
		self.y = s.y
		self.width = s.width
		#color & images
		self.color = s.color
		self.image = s.image
		self.mask_image = s.mask_image
		#display states
		self.showColor = s.showColor
		self.showImage = s.showImage
		self.showMask = s.showMask
