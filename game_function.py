import sys
import pygame as pg


def handle_events(sett,screen,hero,enermies,bullets):
	"""
	处理键盘和鼠标事件
	"""
	for event in pg.event.get():
		if event.type==pg.QUIT:
			sys.exit()

		elif hero.plane==None:
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_RIGHT:
					hero.moving_right = True
				elif event.key == pg.K_LEFT:
					hero.moving_left = True	
				elif event.key==pg.K_UP:
					hero.jumping=True
					pass
				elif event.key==K_DOWN:
					hero.moveing_up=True
				#snip

			elif event.type == pg.KEYUP:
				if event.key == pg.K_RIGHT:
					hero.moving_right = False
				elif event.key == pg.K_LEFT:
					hero.moving_left = False
				elif event.key==pg.K_DOWN:
					hero.moving_up=False		
					pass
				#snip
				
		else:
			#hero驾驶飞机或坦克时
			pass

def update_screen(sett,screen,hero,enermies,bullets):
	"""
	更新屏幕
	"""
	screen.fill(sett.bg_color)
	hero.drawme()
	#snip

	pg.display.flip()

def update_enermies(enermies,hero):
	"""
	更新enermy的位置，判断enermy是否与hero碰撞,若是，将碰撞的enermy存到hero.plane，
	并把hero.plane.driven_by_hero改为True,并在enermies中remove掉这个enermy
	"""
	pass

def update_bullets(bullets,hero,enermies):
	"""
	更新子弹位置，判断子弹是否与hero或enermies碰撞,导弹与其他敌方炮弹是否碰撞
	"""
	bullets[0].update()
	bullets[1].update(bullets)
	bullets[2].update()
	bullets[3].update()
	bullets[4].update(bullets)
	bullets[5].update((hero.rect.centerx,hero.rect.centery))

	#处理子弹命中
	#snip