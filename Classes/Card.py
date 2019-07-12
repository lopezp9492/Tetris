import pygame
from constants import *


class Card(object):
	
	""" Static variables in Card class. """
	TitleCardImage = pygame.image.load("Images/Illuminati_Tittle_Card.png")
	TitleCardMiniImage = pygame.image.load("Images/Illuminati_Tittle_Card60x40.png")
	TitleCardMiniRotatedImage = pygame.image.load("Images/Illuminati_Tittle_Card60x40r.png")
	
	
	def __init__(self):
		self.Image = Card.TitleCardImage
		self.miniImage = Card.TitleCardMiniImage
		self.miniImageRotated = Card.TitleCardMiniRotatedImage
		
		#Width & Height of card
		self.width = 60
		self.height = 40
	
		"""Scree Position && Orientation"""
		self.x  = 0
		self.y = 0
		self.faceUp = True
		self.direction = "up"
		
		#values loaded from file
		self.name = "card name:"
		self.specialAbility = "card ability"
		
		self.directPower = 0
		self.supportPower = 0
		self.resistance = 0
		self.income = 0
		
		self.alignment1 = "none"
		self.alignment2 = "none"
		self.alignment3 = "none"
		
		#default arrow type = o (out)
		self.arrowuP = "o"
		self.arrowuDown= "o"
		self.arrowLeft = "o"
		self.arrowRight = "o"
		
		#values updated during gameplay
		self.megaBucks = 0

	
	def loadFromFile(self, line):
		parts_list = line.split('/')
		for s in parts_list:
			s = s.strip()
			print("[" + s + "]")
		
		
		"""
		self.directPower = parts_list[0]
		self.supportPower = parts_list[1]
		self.resistance = parts_list[2]
		self.income = parts_list[3]
		
		self.alignment1 = parts_list[4]
		self.alignment1 = parts_list[5]
		self.alignment1 = parts_list[6]
		
		self.arrowuP = parts_list[7][0]
		self.arrowuDown= parts_list[7][1]
		self.arrowLeft = parts_list[7][2]
		self.arrowRight = parts_list[7]	[3]
		"""
		self.name  =  parts_list[8].strip()
		image_file_name = "Images/cards/" + self.name  + ".png"
		self.loadImage(image_file_name)
		


	#--- Methods ---
	def flip(self):
		if self.faceUp:
			self.faceUp = False
		else:
			self.faceUp = True


	def collectIncome(self):
		self.megaBucks += income
		
	def draw(self, screen):
		screen.blit(self.miniImage, [self.x, self.y])


	def loadImage(self, image_file_name):
		#load
		self.image = pygame.image.load(image_file_name)
		#scale down to mini size
		self.miniImage = pygame.transform.scale(self.image,(60,40))
		#rotate mini version
		self.miniImageRotated = pygame.transform.rotate(self.image, 90)
		#scale original to wanted size
		self.Image = pygame.transform.scale(self.image, (180,120))
		

	def getImage(self):
		return self.image


	def setPosition(self, pos):
		self.x = pos[0]
		self.y = pos[1]
		
	""" 
	#can not overload in python as in C++ or JAVA
	def setPosition(self, x, y):
		self.x = x
		self.y = y
	"""

	
	def wasClicked(self, pos):
		if pos[0]-self.x > 0 and pos[0]-self.x < self.width:
			if pos[1]-self.y > 0 and pos[1]-self.y < self.height:
				print("Card Click ", pos)
				return True
		return False



