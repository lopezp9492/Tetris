"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
import time
 
import pygame
from Classes import COLORS

from Classes.Background import *
from Classes.TGrid import *

from Classes.Square import *
from Classes.Tetromino import *

from Classes.Tshape import *
from Classes.Oshape import *
from Classes.Ishape import *
from Classes.Zshape import *
from Classes.Sshape import *
from Classes.Jshape import *
from Classes.Lshape import *
from Classes.Pshape import *

todoList = "Next todo: TGrid.clearFullLines "
print(todoList)


pygame.init()
 
# Set the width and height of the screen [width, height]
size = CONSTANTS.WINDOW_SIZE
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")

#Shapes Being Tested
square = Square()
tetromino = Tetromino()
shape = Pshape()

#Background
background = Background(size)
 
#Grid
grid  = TGrid()
grid.centerXposition(size)

#set position of squares
#square.setBase(grid.getPosition)
square.base_x = grid.x
square.base_y = grid.y

shape.setBase([grid.x, grid.y])
#shape.base_x = grid.x
#shape.base_y = grid.y
 
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

t0 = time.time()
fall_time = 1.0
 
# -------- Main Program Loop -----------
while not done:
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			square.moveDown()
			
		# User pressed down on a key
		elif event.type == pygame.KEYDOWN:
        # Figure out if it was an arrow key. If so
        # adjust speed.
			#arrow keys = move keys
			if event.key == pygame.K_LEFT:
				shape.moveLeft()
				if shape.isOutsideOfBounds(grid.rows, grid.cols):
					shape.moveRight()
				
				if grid.squaresOverlap(shape):
					shape.moveRight()
				
				#if(square.x>0):
					#square.moveLeft()
			elif event.key == pygame.K_RIGHT:
				shape.moveRight()
				if shape.isOutsideOfBounds(grid.rows, grid.cols):
					shape.moveLeft()
					
				if grid.squaresOverlap(shape):
					shape.moveLeft()
					
				#if(square.x<grid.cols-1):
					#square.moveRight()
			elif event.key == pygame.K_UP:
				print("up key pressed")
				"""
				#Disabled up Key 
				shape.moveUp()
				if shape.isOutsideOfBounds(grid.rows, grid.cols):
					shape.moveDown()
					
				if grid.squaresOverlap(shape):
					shape.moveDown()
				"""
				
				#if(square.y>0):
					#square.moveUp()
			elif event.key == pygame.K_DOWN:
				shape.moveDown()
				if shape.isOutsideOfBounds(grid.rows, grid.cols):
					shape.moveUp()
					
				if grid.squaresOverlap(shape):
					shape.moveUp()
				#if(square.y<grid.rows-1):
					#square.moveDown()
			#rotate keys
			elif event.key == pygame.K_z:
				shape.rotateLeft()
				if shape.isOutsideOfBounds(grid.rows, grid.cols):
					shape.rotateRight()
					
				if grid.squaresOverlap(shape):
					shape.rotateRight()
				
			elif event.key == pygame.K_x:
				shape.rotateRight()
				if shape.isOutsideOfBounds(grid.rows, grid.cols):
					shape.rotateLeft()
					
				if grid.squaresOverlap(shape):
					shape.rotateRight()
					
			elif event.key == pygame.K_p:
				grid.printSortedList()
 
    # --- Game logic should go here
	if time.time() - t0 > fall_time:
		t0 = time.time()
		
		if shape.isAtBottom(grid.rows):
			grid.add(shape)
			grid.clearFullLines()
			shape.setPosition([5,0])
			
		else:
			shape.moveDown()
			if shape.isOutsideOfBounds(grid.rows, grid.cols):
				shape.moveUp()
				
			if grid.squaresOverlap(shape):
				shape.moveUp()
				#move to start position
				grid.add(shape)
				grid.clearFullLines()
				shape.setPosition([5,0])
		
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
	screen.fill(COLORS.BLACK)
 
    # --- Drawing code should go here
	background.display(screen)
	grid.display(screen)
	#square.display(screen)
	#tetromino.display(screen)
	shape.display(screen)
 
    # --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()
 
    # --- Limit to 60 frames per second
	clock.tick(60)
 
# Close the window and quit.
pygame.quit()
