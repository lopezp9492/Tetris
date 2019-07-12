from Classes.Tetromino import *
from Classes.COLORS import *

class Zshape(Tetromino):
	
	"""static variables"""
	COLOR = COLORS.RED
	
	def __init__(self):
	
		#calll parent constructor
		super().__init__()
		self.type = 'Z'

		#setup own Zshape variables
		self.faceLeft()
		self.setColor(Zshape.COLOR)

	"""  #"""
	"""##"""
	"""#  """
	def faceUp(self):
		self.resetSquares()
		self.orientation = Tetromino.UP
		#self.squares[0]
		self.squares[1].moveUp()
		self.squares[2].moveLeft()
		self.squares[3].moveLeft()
		self.squares[3].moveDown()



	"""##   """
	"""  ## """
	def faceRight(self):
		self.resetSquares()
		self.orientation = Tetromino.RIGHT
		#self.squares[0]
		self.squares[1].moveLeft()
		self.squares[2].moveDown()
		self.squares[3].moveDown()
		self.squares[3].moveRight()


	"""  #"""
	"""##"""
	"""#  """
	def faceDown(self):
		self.faceUp()


	"""##   """
	"""  ## """
	def faceLeft(self):
		self.faceRight()

