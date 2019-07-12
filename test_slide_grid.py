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
from SlideGridClasses.SlideGrid import *


pygame.init()
 
# Set the width and height of the screen [width, height]
size = CONSTANTS.WINDOW_SIZE
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")

#Shapes Being Tested
sg = SlideGrid()

#Background
background = Background(size)
  
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
			#square.moveDown()
			print("hello")
		# User pressed down on a key
		elif event.type == pygame.KEYDOWN:
        # Figure out if it was an arrow key. If so
        # adjust speed.
			#arrow keys = move keys
			if event.key == pygame.K_LEFT:
				sg.moveLeft()
				
			elif event.key == pygame.K_RIGHT:
				sg.moveRight()
					
			elif event.key == pygame.K_UP:
				sg.moveUp()

			elif event.key == pygame.K_DOWN:
				sg.moveDown()

			elif event.key == pygame.K_z:
				print("hey")

			elif event.key == pygame.K_x:
				print("hello")
				
			elif event.key == pygame.K_p:
				print("yeah")
			elif event.key ==pygame.K_r:
				sg.randomize()
		
 
    # --- Game logic should go here
	if time.time() - t0 > fall_time:
		t0 = time.time()
		print("tick")
		
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
	screen.fill(COLORS.BLACK)
 
    # --- Drawing code should go here
	background.display(screen)
	sg.display(screen)
	
    # --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()
 
    # --- Limit to 60 frames per second
	clock.tick(60)
 
# Close the window and quit.
pygame.quit()
