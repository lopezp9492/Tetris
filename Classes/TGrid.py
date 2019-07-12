
from operator import itemgetter, attrgetter, methodcaller
import pygame
from Classes import CONSTANTS
from Classes import COLORS
from Classes.Square import *
from Classes.Tetromino import *
#import copy


""" this class represents the tetromino space """
class TGrid(object):
	
	def __init__(self):
		""" Setup variables in Grid class. """
		
		""" width & height of each square """
		self.cols  = CONSTANTS.GRID_WIDTH#squares
		self.rows = CONSTANTS.GRID_HEIGHT#squares
		self.square_width = CONSTANTS.SQUARE_WIDTH

		self.margin = 5#pixels
		
		"""Grid Base"""
		self.base_x = 0#pixel units
		self.base_y = 0

		"""Grid Position"""
		self.x = 2#square units
		self.y = 2
		
		#color of each tile
		self.color = COLORS.WHITE
		
		
		self.tileImage = pygame.image.load("Images/background tile dark4.png")
		
		self.tileImage = pygame.transform.scale(self.tileImage,(self.square_width,self.square_width))
		

		self.squares = []
		self.full_row_index = -1

	#--- Methods ---#
	
	#Sets the number of rows and columns of the grid
	def setSize(self, r, c):
		self.rows = r
		self.cols = c
		"""del self.grid[:]
		self.initGrid()
		"""

	#sets the position to the given values
	#pos is a tupple, two values in one
	def setPosition(self, pos):
		self.x = pos[0]
		self.y = pos[1]
		
	def getPosition(self):
		x = self.base_x +(self.x*self.square_width)
		y = self.base_y +(self.y*self.square_width)
		pos = [x, y]
		return pos
		
	def add(self, tetromino):
		for s in tetromino.squares:
			#t = copy.deepcopy(s)
			x = Square()
			x.copy(s)
			self.squares.append(x)
	
	#Aligns object to the horizontal center
	def centerXposition(self, window_size):
		self.base_x = 0
		self.base_y = 0
		
		grid_width = self.square_width*self.cols
		self.base_x = int((window_size[0] - grid_width)/2)
		
		#align with grid using modulo
		m = self.base_x%self.square_width
		self.base_x = self.square_width*m
		print("new grid.base_x:", self.base_x)
	
	#Aligns object to the vertical center
	def centerYposition(self, window_size):
		self.base_x = 0
		self.base_y = 0
		
		grid_height = self.square_width*self.rows
		self.y = int((window_size[1] - grid_height)/2)
		
		#align with grid using modulo
		m = self.base_y%self.square_width
		self.base_y = self.square_width*m
		print("new grid.base_y:", self.base_y)

	#Aligns objcect to the center of the screen
	def centerPosition(self, window_size):
		self.centerXposition(window_size)
		self.centerYposition(window_size)

	def display(self,screen):
		self.displayBackground(screen)
		self.displaySquares(screen)
		
	#prints the self.tileImage at each tile position
	def displayBackground(self,screen):
		for row in range(self.rows):
			for column in range(self.cols):
				x_pos = self.base_x + (self.square_width*( self.x + column))
				y_pos = self.base_y + (self.square_width*( self.y + row)) 
				pos = [x_pos, y_pos]
				screen.blit(self.tileImage, pos)
				
	def displaySquares(self, screen):
		for s in self.squares:
			s.display(screen)
	#can be improved by only checking the 4 rows necesary
	def squaresOverlap(self, tetromino):
		for ts in tetromino.squares:
			for ss in self.squares:
				if ts.x == ss.x and ts.y == ss.y:
					return True
	
	def clearFullLines(self):
		#print("checking for full lines")
		#self.printSortedList()
		while self.findFullLine():
			self.clearFullLine()
			self.moveRowsDown()
			
	def findFullLine(self):
		#sort by row, lower first
		self.squares.sort(key=attrgetter('y', 'x'), reverse=True)
		#1 check the count for each row
		square_count = 0
		row_level = self.squares[0].y
		#print( "row level: %d " % row_level)
		for i in range(len(self.squares)):
			#print("y: %d " % self.squares[i].y)
			if self.squares[i].y == row_level:
				square_count+= 1
				if square_count == 10:
					self.full_row_index = self.squares[i].y
					print( "full_row_index: %d " % self.full_row_index)
					return True
			else:
				#print("partial_row_index: %d" % row_level)
				row_level = self.squares[i].y
				square_count = 1
		return False
	
	def clearFullLine(self):
		#print("cfl full_row_index: ", self.full_row_index)
		for s in reversed(self.squares):
			if s.y == self.full_row_index:
				self.squares.remove(s)

	def moveRowsDown(self):
		for s in self.squares:
			if s.y < self.full_row_index:
				s.moveDown()
		
	def __testMethod(self):
		print("this is a private method")
	
	#test method
	def printSortedList(self):
		self.squares.sort(key=attrgetter('y', 'x'), reverse=True)
		for s in self.squares:
			print(s)
		#print(sorted(self.squares, key=attrgetter('x', 'y')))
