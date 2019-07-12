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
from Classes.MSquare import *
from Classes.TUnit import *


todoList = "Test TUnit "
print(todoList)


pygame.init()
 
# Set the width and height of the screen [width, height]
size = CONSTANTS.WINDOW_SIZE
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")

#Objects Being Tested
tUnit1 = TUnit()
tUnit1.setPosition([1,2])

tUnit2 = TUnit()
tUnit2.setPosition([20, 2])
tUnit2.setP2Controls()

#Background
background = Background(size)
 
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

t0 = time.time()
fall_time = 1.0

font  = pygame.font.Font("C:/Windows/Fonts/BRUSHSCI.TTF", 25)
score = 100
text_position = [20,20]
 
# -------- Main Program Loop -----------
while not done:
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			print("mouse click")
		# User pressed down on a key
		elif event.type == pygame.KEYDOWN:
			#
			print(event)
			tUnit1.processInput(event)
			tUnit2.processInput(event)

 
    # --- Game logic should go here
	if time.time() - t0 > fall_time:
		t0 = time.time()
		
		tUnit1.tick()
		tUnit2.tick()

		
		
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
	screen.fill(COLORS.BLACK)
 
    # --- Drawing code should go here
	background.display(screen)
	tUnit1.display(screen)
	tUnit2.display(screen)
	
	
	text  = font.render("Score: " +str(score), True, COLORS.YELLOW)
	screen.blit(text, text_position)
	
 
    # --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()
 
    # --- Limit to 60 frames per second
	clock.tick(60)
 
# Close the window and quit.
pygame.quit()
