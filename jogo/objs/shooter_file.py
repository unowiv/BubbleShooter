import random
from objs.constants import *
from objs.bubble_file import *
from math import sin, cos, radians, degrees, atan2
import pygame as pg


class Shooter():

	def __init__(self, image = 'jogo/images/gun.png', pos = display_rect.center):


		self.pos = pos
		self.pos_x, self.pos_y = pos

		self.initGunImage(image)
		self.initCrossHair()

		self.angle = 0


		self.reload1_pos = (self.pos_x + 7*BUBBLE_RADIUS, self.pos_y - 20)
		self.reload2_pos = (self.pos_x + 9.25*BUBBLE_RADIUS, self.pos_y - 20)
		self.reload3_pos = (self.pos_x + 11.5*BUBBLE_RADIUS, self.pos_y - 20)

		self.fired = Bullet(self.pos, self.angle)
		self.fired.exists = False		
		self.loaded = Bubble(self.pos)
		self.reload1 = Bubble(self.reload1_pos)
		self.reload2 = Bubble(self.reload2_pos)
		self.reload3 = Bubble(self.reload3_pos)



	def initGunImage(self, image):

		self.shooter = pg.image.load(image).convert_alpha()

	
		self.shooter_rect = self.shooter.get_rect()
		self.shooter_w = self.shooter_rect[2]
		self.shooter_h = self.shooter_rect[3]

	
		sf = 00.20
		self.shooter = pg.transform.scale(self.shooter, (int(self.shooter_w * sf), int(self.shooter_h * sf)))

	
		self.shooter_rect = self.shooter.get_rect()
		self.shooter_w = self.shooter_rect[2]
		self.shooter_h = self.shooter_rect[3]


	
	def putInBox(self):

	
		self.shooter_box = pg.Surface((self.shooter_w, self.shooter_h*2), pg.SRCALPHA, 32)
		self.shooter_box.fill((0,0,0,0))

	
		self.shooter_box.blit(self.shooter, (0,0))

	
		self.shooter_box = pg.transform.rotate(self.shooter_box, -90)


	def initCrossHair(self):

	
		pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

	
		crosshair = pygame.image.load('jogo/images/crosshair.png')
		sf = 00.20
		self.crosshair = pg.transform.scale(crosshair, (int(crosshair.get_width() * sf), int(crosshair.get_height() * sf)))
		self.crosshair_rect = self.crosshair.get_rect()

	
	def draw(self):
		display.blit(self.shooter_box, self.pos)

	def draw_line(self):

	
		end = ( (cos(radians(self.angle)) * AIM_LENGTH) + DISP_W/2, DISP_H - (sin(radians(self.angle)) * AIM_LENGTH))
		
		pg.draw.line(display, BLACK, self.pos, end)

	
	def rotate(self, mouse_pos):
		self.draw_line()

		self.crosshair_rect.center = mouse_pos
		display.blit(self.crosshair, self.crosshair_rect)

		
		self.angle = self.calcMouseAngle(mouse_pos)

		
		rotated_box = pg.transform.rotate(self.shooter_box, self.angle)

		
		display.blit(rotated_box, rotated_box.get_rect( center = self.pos))

		


	def draw_bullets(self):

		self.fired.update()
		self.loaded.draw()
		self.reload1.draw()
		self.reload2.draw()
		self.reload3.draw()
		

	def fire(self):

		if self.fired.exists: return

		else:
			rads = radians(self.angle)
			self.fired = Bullet(self.pos, rads, self.loaded.color)
			self.loaded = Bubble(self.pos, self.reload1.color)
			self.reload1 = Bubble(self.reload1_pos, self.reload2.color)
			self.reload2 = Bubble(self.reload2_pos, self.reload3.color)
			self.reload3 = Bubble(self.reload3_pos)

	def calcMouseAngle(self, mouse_pos):
		
		mouse_x, mouse_y = mouse_pos[0], mouse_pos[1]

		
		width = mouse_x - self.pos_x
		height = self.pos_y - mouse_y
		angle = atan2(height,width)
		degree = degrees(angle)		# convert to degrees

		
		return max(min(degree , ANGLE_MAX), ANGLE_MIN)