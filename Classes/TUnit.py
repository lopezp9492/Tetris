from random import randrange

import pygame
from Classes import CONSTANTS
from Classes import COLORS

from Classes.Background import *
from Classes.TGrid import *

from Classes.Tetromino import *

from Classes.Tshape import *
from Classes.Oshape import *
from Classes.Ishape import *
from Classes.Zshape import *
from Classes.Sshape import *
from Classes.Jshape import *
from Classes.Lshape import *
from Classes.Pshape import *


""" this class represents the tetromino space """
class TUnit(object):
	
	"""static variables"""
	TOP = (2,0)
	
	#p2 controls
	p2_up = pygame.K_u
	p2_left = pygame.K_h
	p2_down = pygame.K_j
	p2_right = pygame.K_k
	p2_cw = pygame.K_i
	p2_ccw = pygame.K_y
	p2_space = pygame.K_l
	p2_debug = pygame.K_o
	
	#p3 controls
	p3_up = pygame.K_w
	p3_left = pygame.K_a
	p3_down = pygame.K_s
	p3_right = pygame.K_d
	p3_cw = pygame.K_e
	p3_ccw = pygame.K_q
	p3_space = pygame.K_f
	p3_debug = pygame.K_r

	
	def __init__(self):
		""" Setup variables in Grid class. """
		self.x = 3
		self.y = 3
		
		self.shape = Tetromino()
		self.shape = Ishape()
		self.shape = Oshape()
		self.shape.setImageOff()
		
		self.grid  = TGrid()
		
		self.ghost  = Pshape()
		self.ghost.setColorOff()
		self.ghost.setMaskOff()
		#self.ghost.setImage("Images/circle_r16.png")
		self.ghost.setImage("Images/square_phantom32x32.png")

		#self.next = NextPanel()
		#self.hold = HoldPanel()
		#self.score = ScorePanel()
		#self.stats = StatisticsPanel()

		self.shape.setBase(self.grid.getPosition())
		self.ghost.setBase(self.grid.getPosition())
		
		#default controls
		self.left = pygame.K_LEFT
		self.right = pygame.K_RIGHT
		self.down = pygame.K_DOWN
		self.up = pygame.K_UP
		self.cw = pygame.K_x
		self.ccw = pygame.K_z
		self.space = pygame.K_SPACE
		self.debug = pygame.K_p

	#--- Methods ---#

	#sets the position to the given values
	#pos is a tupple, two values in one
	def setPosition(self, pos):
		self.x = pos[0]
		self.y = pos[1]
		self.grid.setPosition(pos)
		self.shape.setBase(self.grid.getPosition())
		self.ghost.setBase(self.grid.getPosition())

	def getPosition(self):
		#pos = [self.x, self.y]
		return  (self.x, self.y)
		
	def processInput(self, event):
		#LEFT
		if event.key == self.left: 
			self.shape.moveLeft()

			if self.shape.isOutsideOfBounds(self.grid.rows, self.grid.cols):
				self.shape.moveRight()

			if self.grid.squaresOverlap(self.shape):
				self.shape.moveRight()
				
			self.ghost.setPosition(self.shape.getPosition())
			self.fastFall(self.ghost)

			#self.ghost.setXPosition(self.shape.getXPosition())
			#self.fastFall(self.ghost)
		
		#RIGHT
		elif event.key == self.right:
			self.shape.moveRight()
			
			if self.shape.isOutsideOfBounds(self.grid.rows, self.grid.cols):
				self.shape.moveLeft()
				
			if self.grid.squaresOverlap(self.shape):
				self.shape.moveLeft()

			self.ghost.setPosition(self.shape.getPosition())
			self.fastFall(self.ghost)
				
		#UP
		elif event.key == self.up:
			print("up key pressed - hold tetromino")

		#DOWN
		elif event.key == self.down:
			self.shape.moveDown()
			
			if self.shape.isOutsideOfBounds(self.grid.rows, self.grid.cols):
				self.shape.moveUp()
				
			if self.grid.squaresOverlap(self.shape):
				self.shape.moveUp()

		#COUNTER CLOCK WISE
		elif event.key == self.ccw: #pygame.K_z:
			self.shape.rotateLeft()
			
			if self.shape.isOutsideOfBounds(self.grid.rows, self.grid.cols):
				self.shape.rotateRight()
				
			if self.grid.squaresOverlap(self.shape):
				self.shape.rotateRight()
			
			self.ghost.orientation = self.shape.orientation
			self.ghost.setPosition(self.shape.getPosition())
			self.fastFall(self.ghost)
				
		#CLOCK WISE	
		elif event.key == self.cw:
			self.shape.rotateRight()
			
			if self.shape.isOutsideOfBounds(self.grid.rows, self.grid.cols):
				self.shape.rotateLeft()
				
			if self.grid.squaresOverlap(self.shape):
				self.shape.rotateRight()
				
			self.ghost.orientation = self.shape.orientation
			self.ghost.setPosition(self.shape.getPosition())
			self.fastFall(self.ghost)
		
		#SPACE
		elif event.key == self.space:
			self.fastFall(self.shape)
		
		#DEBUG
		elif event.key == self.debug:
			self.grid.printSortedList()

			
	def setP2Controls(self):
		self.up = TUnit.p2_up
		self.left = TUnit.p2_left
		self.down = TUnit.p2_down
		self.right = TUnit.p2_right
		self.cw = TUnit.p2_cw
		self.ccw = TUnit.p2_ccw
		self.space = TUnit.p2_space
		self.debug = TUnit.p2_debug

		
	#moves falling shape down one space per call
	def tick(self):
		if self.shape.isAtBottom(self.grid.rows):
			#copy to grid
			self.grid.add(self.shape)
			#clear full lines
			self.grid.clearFullLines()
			#change shape
			self.shape = self.randomShape()
			#move back to start position
			self.shape.setPosition([5,0])
			#update ghost
			self.ghost = self.setShape(self.shape.type)
			self.ghost.setColorOff()
			self.ghost.setMaskOff()
			self.ghost.setBase(self.grid.getPosition())
			self.ghost.setPosition([5,0])
			self.fastFall(self.ghost)

		else:
			self.shape.moveDown()
			
			if self.shape.isOutsideOfBounds(self.grid.rows, self.grid.cols):
				self.shape.moveUp()
				
			if self.grid.squaresOverlap(self.shape):
				self.shape.moveUp()
				#copy to grid
				self.grid.add(self.shape)
				#clear full lines
				self.grid.clearFullLines()
				#change shape
				self.shape = self.randomShape()
				#move back to start position
				self.shape.setPosition([5,0])
				#update ghost
				self.ghost = self.setShape(self.shape.type)
				self.ghost.setColorOff()
				self.ghost.setMaskOff()
				self.ghost.setBase(self.grid.getPosition())
				self.ghost.setPosition([5,0])
				self.fastFall(self.ghost)


	#shape must be contained within grid
	#else infinite loop happens
	def fastFall(self, shape):
		#print("fast fall method")
		count = 0
		while shape.isOutsideOfBounds(self.grid.rows, self.grid.cols) != True and self.grid.squaresOverlap(shape) != True:
			count +=1
			shape.moveDown()
		#print("count: ", count)
		shape.moveUp()

	def randomShape(self):
		x = randrange(8)
		#print("method: randomShape():  randValue = ", x)
		s = Tetromino()
		if x == 0:
			s = Pshape()
		elif x == 1:
			s =  Lshape()
		elif x == 2:
			s =  Jshape()
		elif x == 3:
			s = Sshape()
		elif x == 4:
			s = Zshape()
		elif x == 5:
			s = Ishape()
		elif x == 6:
			s = Oshape()
		elif x == 7:
			s = Tshape() 
		s.setImageOff()
		s.setBase(self.grid.getPosition())
		return s
		
	def setShape(self, type):
		#print("method: setShape():  type = ", type)
		s = Tetromino()
		if type == 'P':
			s = Pshape()
		elif type == 'L':
			s =  Lshape()
		elif type == 'J':
			s =  Jshape()
		elif type == 'S':
			s = Sshape()
		elif type == 'Z':
			s = Zshape()
		elif type == 'I':
			s = Ishape()
		elif type == 'O':
			s = Oshape()
		elif type == 'T':
			s = Tshape() 
		return s

	def display(self,screen):
		self.grid.display(screen)
		self.ghost.display(screen)
		self.shape.display(screen)

		
	def __testMethod(self):
		print("this is a private method")
