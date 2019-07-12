#import pygame
from Classes.Square import *
import abc

class Tetromino(object):
	#__metaclass__ = abc.ABCMeta
	
	"""static variables"""
	number_of_squares = 4
	UP = 0
	DOWN = 1
	LEFT = 2
	RIGHT = 3
	
	def __init__(self):
	
		self.base_x = 0#pixels
		self.base_y = 0#pixels
	
		self.x = 5#square units
		self.y = 5#square units
				
		self.orientation = Tetromino.UP
		self.type = 'X'

		self.squares = []
		self.initiateSquares()
	
	def initiateSquares(self):
		#add squares to list
		for i in range(Tetromino.number_of_squares):
			s = Square()
			self.squares.append(s)
		#set position
		for s in self.squares:
			s.setPosition([self.x, self.y])
			
	def setColor(self, color):
		for s in self.squares:
			s.setColor(color)
	
	def display(self, screen):
		for s in self.squares:
			s.display(screen)
	
	def setImage(self, image_name):
		for s in self.squares:
			s.setImage(image_name)
	
	def setColorOff(self):
		for s in self.squares:
			s.setColorOff()
			
	def setImageOff(self):
		for s in self.squares:
			s.setImageOff()
			
	def setMaskOff(self):
		for s in self.squares:
			s.setMaskOff()
			
	def setColorOn(self):
		for s in self.squares:
			s.setColorOn()
			
	def setImageOn(self):
		for s in self.squares:
			s.setImageOn()
			
	def setMaskOn(self):
		for s in self.squares:
			s.setMaskOn()
	
	def moveLeft(self):
		self.x-=1
		for s in self.squares:
			s.moveLeft()
			
	def moveRight(self):
		self.x+=1
		for s in self.squares:
			s.moveRight()
			
	def moveDown(self):
		self.y+=1
		for s in self.squares:
			s.moveDown()
			
	def moveUp(self):
		self.y-=1
		for s in self.squares:
			s.moveUp()
			
	#sets all squares to the same position
	def resetSquares(self):
		for s in self.squares:
			s.setPosition([self.x, self.y])

	#returns true if any of the blocks overlap another tetromino
	#	not optimal
	def overlaps(self, tetromino):
		for s in self.squares:
			for z in tetromino.squares:
				if s.x == z.x and s.y == z.y:
					return True
					
	def isOutsideOfBounds(self, rows, cols):
		for s in self.squares:
			if s.x < 0 or s.y<0 or s.x>(cols-1) or s.y > (rows-1):
				return True

	def isAtBottom(self, rows):
		for s in self.squares:
			if s.y ==rows-1:
				return True

	"""rotates the tetromino shape clockwise"""
	def rotateRight(self):
		if self.orientation == Tetromino.UP:
			self.faceRight()
			
		elif self.orientation == Tetromino.RIGHT:
			self.faceDown()
			
		elif self.orientation == Tetromino.DOWN:
			self.faceLeft()
			
		elif self.orientation == Tetromino.LEFT:
			self.faceUp()

	"""rotates the tetromino shape counter-clockwise"""
	def rotateLeft(self):
		if self.orientation == Tetromino.UP:
			self.faceLeft()
			
		elif self.orientation == Tetromino.LEFT:
			self.faceDown()
			
		elif self.orientation == Tetromino.DOWN:
			self.faceRight()
			
		elif self.orientation == Tetromino.RIGHT:
			self.faceUp()

	def setBase(self, pos):
		for s in self.squares:
			s.setBase(pos)

	def setPosition(self, pos):
		self.x = pos[0]
		self.y = pos[1]
		for s in self.squares:
			s.setPosition(pos)
			
		if self.orientation == Tetromino.UP:
			self.faceUp()
		elif self.orientation == Tetromino.DOWN:
			self.faceDown()
		elif self.orientation == Tetromino.RIGHT:
			self.faceRight()
		elif self.orientation == Tetromino.LEFT:
			self.faceLeft()
		
	def getPosition(self):
		return self.squares[0].getPosition()
			
	"""Abstract Methods"""
		
	@abc.abstractmethod
	def faceUp(self):
		"""rotates the tetromino to the up orientation"""
	
	@abc.abstractmethod
	def faceRight(self):
		"""rotates the tetromino to the right orientation"""
	
	@abc.abstractmethod
	def faceDown(self):
		"""rotates the tetromino to the down orientation"""
	
	@abc.abstractmethod
	def faceLeft(self):
		"""rotates the tetromino to the left orientation"""