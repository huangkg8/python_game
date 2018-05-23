import sys
import pygame as pg


def handle_events(sett,screen,hero,enermies,bullets):
	"""
	处理键盘和鼠标事件
	"""
	for event in pg.event.get():
		if event.type==pg.QUIT:
			sys.exit()


		#hero没有驾驶敌机
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
					hero.moveing_up=True  #攀爬
				elif event.key==K_SPACE:
					#开火
					
			elif event.type == pg.KEYUP:
				if event.key == pg.K_RIGHT:
					hero.moving_right = False
				elif event.key == pg.K_LEFT:
					hero.moving_left = False
				elif event.key==pg.K_DOWN:
					hero.moving_up=False		
				
				

		#hero驾驶飞机或坦克时		
		else:
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_RIGHT:
					hero.plane.moving_right = True
				elif event.key == pg.K_LEFT:
					hero.plane.moving_left = True	
				elif event.key==pg.K_UP:
					hero.plane.moving_up=True
				elif event.key==K_DOWN:
					hero.plane.moving_down=True
				elif event.key==K_SPACE:
					#开火,不同战机不同子弹
					if str(type(hero.plane))=="<class '__main__.Ordin_plane'>":
						
					elif str(type(hero.plane))=="<class '__main__.Multi_plane'>":

					elif str(type(hero.plane))=="<class '__main__.Missile_plane'>":	
						bullet2=Bullet2(self,sett,screen,shooter,byhero,hero.missile_target)
						bullets[2].add(bullet2)

			elif event.type == pg.KEYUP:
				if event.key == pg.K_RIGHT:
					hero.plane.moving_right = False
				elif event.key == pg.K_LEFT:
					hero.plane.moving_left = False
				elif event.key==pg.K_UP:
					hero.plane.moving_up=False
				elif event.key==pg.K_DOWN:
					hero.plane.moving_down=False	

			elif #鼠标事件:
				if str(type(hero.plane))=="<class '__main__.Missile_plane'>":
					#如果鼠标点击某架敌机，则将其作为导弹target，并存入hero.missle_target
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
	更新子弹位置，判断子弹是否与hero或enermies碰撞,导弹与敌方炮弹是否碰撞
	"""
	bullets[0].update()
	bullets[1].update(bullets)
	bullets[2].update()
	bullets[3].update()
	bullets[4].update(bullets)
	bullets[5].update()

	#处理子弹命中
	#snip