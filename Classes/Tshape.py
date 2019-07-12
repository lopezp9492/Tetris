from Classes.Tetromino import *
from Classes.COLORS import *

class Tshape(Tetromino):
	
	"""static variables"""
	COLOR = COLORS.GREY
	
	def __init__(self):
	
		#calll parent constructor
		super().__init__()
		self.type = 'T'
		
		#setup own tshape variables]
		self.faceDown()
		self.setColor(Tshape.COLOR)
		
	def rotateRight(self):
		if self.orientation == Tetromino.UP:
			self.faceRight()
			
		elif self.orientation == Tetromino.RIGHT:
			self.faceDown()
			
		elif self.orientation == Tetromino.DOWN:
			self.faceLeft()
			
		elif self.orientation == Tetromino.LEFT:
			self.faceUp()
			
			
	def rotateLeft(self):
		if self.orientation == Tetromino.UP:
			self.faceLeft()
			
		elif self.orientation == Tetromino.LEFT:
			self.faceDown()
			
		elif self.orientation == Tetromino.DOWN:
			self.faceRight()
			
		elif self.orientation == Tetromino.RIGHT:
			self.faceUp()

	"""  #   """
	"""###"""
	def faceUp(self):
		self.resetSquares()
		self.orientation = Tetromino.UP
		#self.squares[0]
		self.squares[1].moveRight()
		self.squares[2].moveLeft()
		self.squares[3].moveUp()

		
		"""#   """
		"""##"""
		"""#   """
	def faceRight(self):
		self.resetSquares()
		self.orientation = Tetromino.RIGHT
		#self.squares[0]
		self.squares[1].moveDown()
		self.squares[2].moveUp()
		self.squares[3].moveRight()


	"""###"""
	"""  #   """
	def faceDown(self):
		self.resetSquares()
		self.orientation = Tetromino.DOWN
		#self.squares[0]
		self.squares[1].moveLeft()
		self.squares[2].moveRight()
		self.squares[3].moveDown()
	
		"""  #"""
		"""##"""
		"""  #"""
	def faceLeft(self):
		self.resetSquares()
		self.orientation = Tetromino.LEFT
		#self.squares[0]
		self.squares[1].moveUp()
		self.squares[2].moveDown()
		self.squares[3].moveLeft()
	
			
