from Classes.Tetromino import *
from Classes.COLORS import *

class Sshape(Tetromino):
	
	
	"""static variables"""
	COLOR = COLORS.GREEN

	
	def __init__(self):
	
		#calll parent constructor
		super().__init__()
		self.type = 'S'

		
		#setup own Zshape variables
		self.faceRight()
		self.setColor(Sshape.COLOR)

	"""#  """
	"""##"""
	"""  #"""
	def faceUp(self):
		self.resetSquares()
		self.orientation = Tetromino.UP
		#self.squares[0]
		self.squares[1].moveUp()
		self.squares[2].moveRight()
		self.squares[3].moveRight()
		self.squares[3].moveDown()



	"""   ## """
	"""##    """
	def faceRight(self):
		self.resetSquares()
		self.orientation = Tetromino.RIGHT
		#self.squares[0]
		self.squares[1].moveRight()
		self.squares[2].moveDown()
		self.squares[3].moveDown()
		self.squares[3].moveLeft()


	"""#  """
	"""##"""
	"""  #"""
	def faceDown(self):
		self.faceUp()


	"""   ## """
	"""##    """
	def faceLeft(self):
		self.faceRight()

