import time, random
from objs.constants import *
from objs.bubble_file import *
from objs.grid_file import *
from objs.shooter_file import *
from objs.game_objects import *

#from menuprincipal import *
import pygame as pg
import os
pg.init()

def main():

	# Criação background
	background = Background()

	# Inicia a gun
	gun = Shooter(pos = BOTTOM_CENTER)
	gun.putInBox()	

	grid_manager = GridManager()
	game = Game()	
	cheat_manager = CheatManager(grid_manager, gun)

	# Começando posição mouse
	mouse_pos = (DISP_W/2, DISP_H/2)
	
	while not game.over:		

		# Sai quando pressionar 
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				quit()

		
			if event.type == pg.MOUSEMOTION: mouse_pos = pg.mouse.get_pos()

			if event.type == pg.MOUSEBUTTONDOWN: gun.fire()
			
			if event.type == pg.KEYDOWN:
				cheat_manager.view(event) 

				# Ctrl+C para sair
				if event.key == pg.K_c and pg.key.get_mods() & pg.KMOD_CTRL:
					pg.quit()
					quit()

		
		background.draw()				# Desenha Backgorund	

		grid_manager.view(gun, game)	# Check collision with bullet and update grid as needed		

		gun.rotate(mouse_pos)			# Rotação da gun	
		gun.draw_bullets()				# Desenha e atualiza as bolinhas	

		game.drawScore()				# Desenha o score na tela

		pg.display.update()		
		clock.tick(60)					#Seta FPS

	game.gameOverScreen(grid_manager, background)

	return

if __name__ == '__main__': 
	while True: main()