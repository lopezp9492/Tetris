from Classes.Tetromino import *
from Classes.COLORS import *

class Jshape(Tetromino):
	
	
	"""static variables"""
	COLOR = COLORS.ORANGE
	
	def __init__(self):
	
		#calll parent constructor
		super().__init__()
		self.type = 'J'
		
		#setup own Zshape variables
		self.faceLeft()
		self.setColor(Jshape.COLOR)

	"""  #"""
	"""  O"""
	"""##"""
	def faceUp(self):
		self.resetSquares()
		self.orientation = Tetromino.UP
		#self.squares[0]
		self.squares[1].moveUp()
		self.squares[2].moveDown()
		self.squares[3].moveDown()
		self.squares[3].moveLeft()


	"""#"""
	"""#O##"""
	def faceRight(self):
		self.resetSquares()
		self.orientation = Tetromino.RIGHT
		#self.squares[0]
		self.squares[1].moveRight()
		self.squares[2].moveLeft()
		self.squares[3].moveLeft()
		self.squares[3].moveUp()

	
	"""##""" 
	"""O  """
	"""#  """
	def faceDown(self):
		self.resetSquares()
		self.orientation = Tetromino.DOWN
		#self.squares[0]
		self.squares[1].moveDown()
		self.squares[2].moveUp()
		self.squares[3].moveUp()
		self.squares[3].moveRight()



	"""##O#"""
	"""       #"""
	def faceLeft(self):
		self.resetSquares()
		self.orientation = Tetromino.LEFT
		#self.squares[0]
		self.squares[1].moveLeft()
		self.squares[2].moveRight()
		self.squares[3].moveRight()
		self.squares[3].moveDown()

