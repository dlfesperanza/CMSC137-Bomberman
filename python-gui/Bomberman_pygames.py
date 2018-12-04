#!/usr/bin/env python
#Reference : https://github.com/xamox/pygame/blob/master/examples/aliens.py

import os.path
import pygame
from pygame.locals import *

SCREEN = Rect(0, 0, 900, 600)
OBJ_WIDTH = 40
OBJ_HEIGHT = 40
P_WIDTH = 30
P_HEIGHT = 30

if not pygame.image.get_extended():
    raise SystemExit("Sorry, extended image module required")

#Will need documentation
images_dir = os.path.split(os.path.abspath(__file__))[0]

def load_image(file):

	file = os.path.join(images_dir, 'images', file)
	try:
		surface = pygame.image.load(file)
	except pygame.error:
		raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
	return surface.convert()

def load_images(*files):

	images = []
	for file in files:
		images.append(load_image(file))
	return images

def file_reader(): #Reads the map

	map_data = []
	file_read = open("map.csv","r")
	
	for line in file_read:
		line = line[:-1]
		line = line.split(",")
		map_data.append(line)
	return map_data

#Game Classes

class Wood(pygame.sprite.Sprite):

	def __init__(self, x_pos, y_pos):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = pygame.transform.scale(load_image('box.png'), (OBJ_WIDTH - 1, OBJ_HEIGHT - 1))
		self.rect = Rect(x_pos, y_pos, OBJ_WIDTH, OBJ_HEIGHT)

	#Might need if an animation is planned
	#def update(self):

class Metal(pygame.sprite.Sprite):

	def __init__(self, x_pos, y_pos, image):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = pygame.transform.scale(image, (OBJ_WIDTH, OBJ_HEIGHT))
		self.rect = Rect(x_pos, y_pos, OBJ_WIDTH, OBJ_HEIGHT)

# class Grass(pygame.sprite.Sprite):

# 	def __init__(self, x_pos, y_pos):
# 		pygame.sprite.Sprite.__init__(self)
# 		self.image = pygame.transform.scale(load_image('grass.png'), (OBJ_WIDTH - 1, OBJ_HEIGHT - 1))
# 		self.rect = Rect(x_pos, y_pos, OBJ_WIDTH, OBJ_HEIGHT)

class Player(pygame.sprite.Sprite):

	speed = 2
	images = []
	bounce = 24

	def __init__(self, x_pos, y_pos):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = pygame.transform.scale(self.images[0], (P_WIDTH, P_HEIGHT))
		self.rect = Rect(x_pos, y_pos, P_WIDTH, P_HEIGHT)
		self.origtop = self.rect.top
		self.origbot = self.rect.bottom

	def move(self, x_dir, y_dir):

		if y_dir < 0:
			#if(self.rect.colliderect())
			self.image = pygame.transform.scale(self.images[1], (P_WIDTH, P_HEIGHT))
			self.rect.move_ip(0, y_dir * self.speed)
		elif y_dir > 0:
			self.image = pygame.transform.scale(self.images[2], (P_WIDTH, P_HEIGHT))
			self.rect.move_ip(0, y_dir * self.speed)

		if x_dir < 0:
			self.image = pygame.transform.scale(pygame.transform.flip(self.images[5], True, False), (P_WIDTH, P_HEIGHT))
			self.rect.move_ip(x_dir * self.speed, 0)
		elif x_dir > 0:
			self.image = pygame.transform.scale(self.images[5], (P_WIDTH, P_HEIGHT))
			self.rect.move_ip(x_dir * self.speed, 0)

		self.rect = self.rect.clamp(SCREEN)

def main(winstyle = 0):
	#print("haha")
	pygame.init()
	winstyle = 0
	bestdepth = pygame.display.mode_ok(SCREEN.size, winstyle, 32)
	screen = pygame.display.set_mode(SCREEN.size, winstyle, bestdepth)

	metal_images = load_images('wall1.png', 'wall2.png')
	Player.images = load_images('player.png', 'player-1.png', 'player-2.png', 'player-3.png', 
								'player-4.png','player-5.png', 'player-6.png', 'player-7.png', 
								'player-8.png','player-9.png', 'player-10.png')

	bg_image = load_image('grass.png')
	bg_image = pygame.transform.scale(bg_image, (900, 600))
	#bg_image = pygame.transform.scale(load_image('grass.png'), (900,600))
	background = pygame.Surface(SCREEN.size)
	for x in range(0, SCREEN.width, bg_image.get_width()):
		background.blit(bg_image, (x, 0))

	screen.blit(background, (0, 0))
	pygame.display.flip()

	exit = False
	clock = pygame.time.Clock()
	map_data = file_reader()

	wood_tiles = pygame.sprite.Group()
	metal_tiles = pygame.sprite.Group()
	all = pygame.sprite.RenderUpdates()

	Wood.containers = wood_tiles, all
	Metal.containers = metal_tiles, all
	Player.containers = all

	for row in range(0, len(map_data)):
		for col in range(0, len(map_data)):
			if map_data[row][col] == 'm':
				all.add(Metal(col * OBJ_WIDTH, row * OBJ_HEIGHT, metal_images[1]))
			elif map_data[row][col] == 'w':
				all.add(Metal(col * OBJ_WIDTH, row * OBJ_HEIGHT, metal_images[0]))
			elif map_data[row][col] == 'b':
				all.add(Wood(col * OBJ_WIDTH, row * OBJ_HEIGHT))

	player = Player(40, 40)

	#CHANGE, need to determine exit condition based on players remaining
	while not exit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit = True

		keypress = pygame.key.get_pressed()

		left_right = keypress[K_RIGHT] - keypress[K_LEFT]
		up_down = keypress[K_DOWN] - keypress[K_UP]
		player.move(left_right, up_down)

		all.clear(screen, background)
		all.update()

		#Modularize this
		for walls in metal_tiles:
			if player.rect.colliderect(walls.rect):
				if left_right < 0:
					player.rect.move_ip(2, 0)
				elif left_right > 0:
					player.rect.move_ip(-2, 0)

				if up_down < 0:
					player.rect.move_ip(0, 2)
				elif up_down > 0:
					player.rect.move_ip(0, -2)

		for boxes in wood_tiles:
			if player.rect.colliderect(boxes.rect):
				if left_right < 0:
					player.rect.move_ip(2, 0)
				elif left_right > 0:
					player.rect.move_ip(-2, 0)

				if up_down < 0:
					player.rect.move_ip(0, 2)
				elif up_down > 0:
					player.rect.move_ip(0, -2)

		dirty = all.draw(screen)
		pygame.display.update(dirty)
		clock.tick(60)

	pygame.quit()

if __name__ == '__main__':
	main()