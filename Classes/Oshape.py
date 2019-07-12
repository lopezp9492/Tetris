from Classes.Tetromino import *
from Classes.COLORS import *

class Oshape(Tetromino):
	
	
	"""static variables"""
	COLOR = COLORS.BLUE
	
	def __init__(self):
	
		#calll parent constructor
		super().__init__()
		self.type = 'O'
		
		#setup own tshape variables]
		self.faceUp()
		self.setColor(Oshape.COLOR)




	"""##"""
	"""##"""
	def faceUp(self):
		self.resetSquares()
		self.orientation = Tetromino.UP
		#self.squares[0]
		self.squares[1].moveRight()
		self.squares[2].moveDown()
		self.squares[3].moveDown()
		self.squares[3].moveRight()


	"""##"""
	"""##"""
	def faceRight(self):
		self.resetSquares()
		self.orientation = Tetromino.RIGHT
		#self.squares[0]
		self.squares[1].moveRight()
		self.squares[2].moveDown()
		self.squares[3].moveDown()
		self.squares[3].moveRight()


	"""##"""
	"""##"""
	def faceDown(self):
		self.resetSquares()
		self.orientation = Tetromino.DOWN
		#self.squares[0]
		self.squares[1].moveRight()
		self.squares[2].moveDown()
		self.squares[3].moveDown()
		self.squares[3].moveRight()


	"""##"""
	"""##"""
	def faceLeft(self):
		self.resetSquares()
		self.orientation = Tetromino.LEFT
		#self.squares[0]
		self.squares[1].moveRight()
		self.squares[2].moveDown()
		self.squares[3].moveDown()
		self.squares[3].moveRight()

