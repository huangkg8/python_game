import sys
import pygame as pg
from pygame.sprite import Group
from settings import Settings
import game_function as gf
from hero import Hero
from enermy import *
from bullet import *
from background import Background

def run_game():
	pg.init()
	sett=Settings()
	screen=pg.display.set_mode((sett.screen_width,sett.screen_height))
	pg.display.set_caption("Super Hijacker")

	#创建hero
	hero=Hero(screen,sett)

	#创建存储敌机的编组
	enemies=Group()
	
	#创建存储子弹的编组
	#bullets[0],bullets[1],bullets[2]分别为存储hero发射的普通子弹、多核弹、导弹的编组，
	#bullets[3],bullets[4],bullets[5]分别为存储enermies发射的普通子弹、多核弹、导弹的编组
	bullets=[]
	for i in range(6):
		bullet=Group()
		bullets.append(bullet)
	
	#游戏主循环
	while True:
		gf.handle_events(sett,screen,hero,enemies,bullets)
		hero.update()
		gf.update_bullets(bullets,hero,enemies)
		gf.update_enermies(enemies,hero)
		gf.update_screen(sett,screen,hero,enemies,bullets)



run_game()
