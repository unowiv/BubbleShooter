import time, random
from objs.constants import *
from objs.bubble_file import *
from objs.grid_file import *
from objs.shooter_file import *
from objs.game_objects import *

import pygame as pg
import os
pg.init()


def main():

	# Criação background
	background = Background()

	# Inicialize a arma, posicione na parte inferior central da tela
	gun = Shooter(pos = BOTTOM_CENTER)
	gun.putInBox()	

	grid_manager = GridManager()
	game = Game()	
	cheat_manager = CheatManager(grid_manager, gun)

	# Iniciando a posição do mouse
	mouse_pos = (DISP_W/2, DISP_H/2)
	
	while not game.over:		

	# sai quando você pressiona x
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				quit()

			#posição do mouse
			if event.type == pg.MOUSEMOTION: mouse_pos = pg.mouse.get_pos()
				
			# se você clicar, dispara uma bala
			if event.type == pg.MOUSEBUTTONDOWN: gun.fire()
			
			if event.type == pg.KEYDOWN:
				cheat_manager.view(event) 

				# Ctrl+C para sair
				if event.key == pg.K_c and pg.key.get_mods() & pg.KMOD_CTRL:
					pg.quit()
					quit()

		
		background.draw()				# Desenhe BG primeiro

		grid_manager.view(gun, game)	# Verifique a colisão com o marcador e atualize a grade conforme necessário	

		gun.rotate(mouse_pos)			#Gire a arma se o mouse for movido
		gun.draw_bullets()			# Desenhe e atualize marcadores e recarregue
		
		game.drawScore()				# pontuação do empate

		pg.display.update()		
		clock.tick(60)					# 60 FPS

	game.gameOverScreen(grid_manager, background)

	return

if __name__ == '__main__': 
	while True: main()
