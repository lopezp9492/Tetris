"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
from Classes.Square import *
from Classes.Tetromino import *
from Classes.Tshape import *
from Classes.Oshape import *
from Classes.Ishape import *
from Classes.Zshape import *
from Classes.Sshape import *





# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")

#Shapes Being Tested
square = Square()
tetromino = Tetromino()
shape = Sshape()
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
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
			elif event.key == pygame.K_RIGHT:
				shape.moveRight()
			elif event.key == pygame.K_UP:
				shape.moveUp()
			elif event.key == pygame.K_DOWN:
				shape.moveDown()
			#rotate keys
			elif event.key == pygame.K_z:
				shape.rotateLeft()
				
			elif event.key == pygame.K_x:
				shape.rotateRight()
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
	screen.fill(BLACK)
 
    # --- Drawing code should go here
	square.display(screen)
	tetromino.display(screen)
	shape.display(screen)
 
    # --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()
 
    # --- Limit to 60 frames per second
	clock.tick(60)
 
# Close the window and quit.
pygame.quit()
