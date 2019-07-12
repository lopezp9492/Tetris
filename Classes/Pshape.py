from Classes.Tetromino import *
from Classes.COLORS import *

class Pshape(Tetromino):
	
	"""static variables"""
	COLOR = COLORS.DARK_GREY
	
	def __init__(self):
	
		#calll parent constructor
		super().__init__()
		self.type = 'P'
		
		#setup own Pshape variables

		#add extra square to list and set its position
		s = Square()
		self.squares.append(s)
		self.squares[4].setPosition([self.x, self.y])
		
		#re-organize
		self.faceUp()
		self.setColor(Pshape.COLOR)

	"""##"""
	"""##"""
	"""#  """
	def faceUp(self):
		self.resetSquares()
		self.orientation = Tetromino.UP
		#self.squares[0]
		self.squares[1].moveRight()
		self.squares[2].moveDown()
		self.squares[3].moveDown()
		self.squares[3].moveRight()

		self.squares[4].moveDown()
		self.squares[4].moveDown()



	"""###"""
	"""  ##"""
	def faceRight(self):
		self.resetSquares()
		self.orientation = Tetromino.RIGHT
		#self.squares[0]
		self.squares[1].moveRight()
		self.squares[2].moveDown()
		self.squares[3].moveDown()
		self.squares[3].moveRight()

		self.squares[4].moveLeft()

	"""  #"""
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

		self.squares[4].moveRight()
		self.squares[4].moveUp()


	"""###"""
	"""##  """
	def faceLeft(self):
		self.resetSquares()
		self.orientation = Tetromino.LEFT
		#self.squares[0]
		self.squares[1].moveRight()
		self.squares[2].moveDown()
		self.squares[3].moveDown()
		self.squares[3].moveRight()
		
		self.squares[4].moveRight()
		self.squares[4].moveRight()
		self.squares[4].moveDown()


