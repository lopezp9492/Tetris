import pygame
#from Classes import CONSTANTS
from Classes import COLORS
from Classes.Square import *
from random import randrange

class SlideGrid(object):
	def __init__(self):
		
		self.cols  = 4#squares
		self.rows = 4#squares
		self.square_width = 100
		
		#grid position
		self.x = 40#pixels
		self.y = 40#pixels
		
		#cursor position
		self.cx = 3
		self.cy = 3
		
		self.color = COLORS.WHITE
		self.tileImage = pygame.image.load("Images/background tile dark4.png")
		self.tileImage = pygame.transform.scale(self.tileImage,(self.square_width,self.square_width))
		
		self.squares = []
		for i in range(self.rows):
			for j in range(self.cols):
				s = Square()
				s.setPosition([i,j])
				s.setBase([self.x, self.y])
				s.setWidth(self.square_width)
				
				image_name = "c-" + str(j) + "-" + str(i) + ".jpeg"
				t_image = pygame.image.load("SlideGridImages/" + image_name)
				
				s.setImage(t_image)
				#s.setMaskOff()
				self.squares.append(s)
		#remove last item
		#self.squares.pop()
		del self.squares[-1]
			
			
	def display(self, screen):
		self.displaySquares(screen)
		self.displayBackground(screen)
			
	def displaySquares(self, screen):
		for s in self.squares:
			s.displayImage(screen)
			
	def displayBackground(self, screen):
		pixel_x = self.x + (self.cx*self.square_width)
		pixel_y = self.y + (self.cy*self.square_width)
		screen.blit(self.tileImage, [pixel_x, pixel_y])

			
	def moveRight(self):
		for s in self.squares:
			if s.x+1 == self.cx and s.y == self.cy:
				s.moveRight()
				self.cx -=1
				return
				
	def moveLeft(self):
		for s in self.squares:
			if s.x-1 == self.cx and s.y == self.cy:
				s.moveLeft()
				self.cx +=1
				return
				
	def moveUp(self):
		for s in self.squares:
			if s.x == self.cx and s.y == self.cy+1:
				s.moveUp()
				self.cy+=1
				return
				
	def moveDown(self):
		for s in self.squares:
			if s.x == self.cx and s.y == self.cy-1:
				s.moveDown()
				self.cy-=1
				return
				
	def randomize(self):
		rand_counter = 20
		for i in range(rand_counter):
			x = randrange(4)
			if x == 0:
				self.moveRight()
			elif x == 1:
				self.moveLeft()
			elif x == 2:
				self.moveDown()
			elif x == 3:
				self.moveUp()
		