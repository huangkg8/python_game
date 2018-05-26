import sys
import pygame as pg
from bullet import *

def handle_events(sett,screen,hero,enemies,bullets):
	"""
	处理键盘和鼠标事件
	"""

	for event in pg.event.get():
		if event.type==pg.QUIT:
			sys.exit()

		elif event.type == pg.KEYDOWN:
			handle_keydown(sett,event,hero,bullets)
				
		elif event.type == pg.KEYUP:
			handle_keyup(sett,event,hero)

		elif event.type==pg.MOUSEBUTTONDOWN:
			mouse_x,mouse_y=pg.mouse.get_pos()
			handle_mouse(mouse_x, mouse_y, hero, enemies)			


def handle_keydown(sett,screen,event,hero,bullets):
	if event.key==K_p:
		sett.game_active = not sett.game_active

	#没有开敌机
	elif not hero.plane:
		#移动
		if event.key == pg.K_RIGHT:
			hero.moving_right = True
		elif event.key == pg.K_LEFT:
			hero.moving_left = True	
		elif event.key==pg.K_UP:
			hero.jumping=True
		elif event.key==K_DOWN:
			hero.moveing_up=True  #攀爬

		#瞄准，开火
		elif event.key==K_d:
			hero.shoot_dir+=sett.dir_factor
			if hero.shoot_dir>360:
				hero.shoot_sir=sett.dir_factor
		elif event.key==K_c:
			hero.shoot_dir-=sett.dir_factor
			if hero.shoot_dir<0:
				hero.shoot_dir=360-sett.dir_factor
		elif event.key==K_SPACE:
			bullet0=Bullet0(sett, screen, hero, hero.shoot_dir, True)
			bullets[0].add(bullet0)

		#检测一下能否组合键
		
	#开敌机		
	else:
		#移动
		if event.key == pg.K_RIGHT:
			hero.plane.moving_right = True
		elif event.key == pg.K_LEFT:
			hero.plane.moving_left = True	
		elif event.key==pg.K_UP:
			if str(type(hero.plane))!="<class '__main__.Tank'>"
				hero.plane.moving_up=True
		elif event.key==K_DOWN:
			if str(type(hero.plane))!="<class '__main__.Tank'>"
				hero.plane.moving_down=True

		#瞄准，开火
		elif event.key==K_d:
			hero.shoot_dir+=sett.dir_factor
			if hero.shoot_dir>360:
				hero.shoot_sir=sett.dir_factor
		elif event.key==K_c:
			hero.shoot_dir-=sett.dir_factor
			if hero.shoot_dir<0:
				hero.shoot_dir=360-sett.dir_factor
		elif event.key==K_SPACE:
			#开火,不同战机不同子弹
			if str(type(hero.plane))=="<class '__main__.Ordin_plane'>":
				bullet0=Bullet0(sett, screen, hero.plane, hero.shoot_dir, True)
				bullets[0].add(bullet0)
			elif str(type(hero.plane))=="<class '__main__.Multi_plane'>":
				bullet1=Bullet1(sett, screen, hero.plane, hero.shoot_dir, True)
				bullets[1].add(bullet1)
			elif str(type(hero.plane))=="<class '__main__.Missile_plane'>":	
				bullet2=Bullet2(sett,screen,hero.plane,hero.missile_target,True)
				bullets[2].add(bullet2)	 
			elif str(type(hero.plane))=="<class '__main__.Tank'>":
				pass

		elif event.key==K_g:
			#离开敌机
			hero.plane=None
			hero.jumping=True


def handle_keyup(event,hero):
	#没有开敌机
	if not hero.plane:
		if event.key == pg.K_RIGHT:
			hero.moving_right = False
		elif event.key == pg.K_LEFT:
			hero.moving_left = False
		elif event.key==pg.K_DOWN:
			hero.moving_up=False

	#开敌机
	else:	
		if event.key == pg.K_RIGHT:
			hero.plane.moving_right = False
		elif event.key == pg.K_LEFT:
			hero.plane.moving_left = False
		elif event.key==pg.K_UP:
			hero.plane.moving_up=False
		elif event.key==pg.K_DOWN:
			hero.plane.moving_down=False	


def handle_mouse(mouse_x,mouse_y,hero,enemies):
	if str(type(hero.plane))=="<class '__main__.Missile_plane'>":
		#如果鼠标点击某架敌机，则将其作为导弹target，并存入hero.missle_target
		pass	


def update_screen(sett,screen,hero,enemies,bullets):
	"""
	更新屏幕
	"""
	screen.fill(sett.bg_color)
	for i in range(6):
		bullets[i].drawme()
	enemies.drawme()
	hero.drawme()

	pg.display.flip()



def update_enemies(enemies,hero):
	"""
	生成新enemy
	更新enemy的位置或发射子弹，判断enemy是否与hero碰撞,若是，将碰撞的enemy存到hero.plane，
	并把hero.plane.jackedTime记录为当前时间，并在enemies中remove掉这个enemy
	"""
	enemies.update()
	if not hero.plane:
		jacked_enemy=pg.sprite.spritecollideany(hero,enemies)
		if jacked_enemy:
			hero.plane=jacked_enemy

			#飞机要左右反过来
			hero.plane.image=pg.image.load('image/enemyx') 
			hero.plane.rect = hero.plane.image.get_rect()
			hero.plane.rect.centerx, hero.plane.rect.centery=jacked_enemy.rect.centerx, jacked_enemy.rect.centery
			hero.plane.shoot_dir=0
			#开始倒计时
			hero.plane.jackedTime=time.clock()
			enemies.remove(jacked_enemy)
	else:
		enemy_crash=pg.sprite.spritecollideany(hero.plane,enemies)
		if enemy_crash:
			hero.plane=None
			hero.falling=True
			hero.life-=1
			if hero.life<=0:
				print('Game over!')
				sett.game_active=False
			enemies.remove(enemy_crash)


def update_bullets(sett,bullets,hero,enemies):
	"""
	更新子弹位置，判断子弹是否与hero或enemies碰撞,导弹与敌方炮弹是否碰撞
	"""
	bullets[0].update()
	bullets[1].update(bullets)
	bullets[2].update()
	bullets[3].update()
	bullets[4].update(bullets)
	bullets[5].update()

	me=hero.plane if hero.plane else hero
	#处理子弹命中
	#hero中弹
	for i in range(3):
		bullet_hit=pg.sprite.spritecollideany(me,bullets[i+3])
		if bullet_hit:
			me.life-=bullet_hit.lethality
			if me.life<=0:
				if str(type(me))=="<class '__main__.Hero'>"：
					print('Game over!')
					sett.game_active=False
				else:
					#驾驶的敌机毁灭则主角生命值减一
					hero.life-=1
					hero.plane=None
					if hero.life<=0:
						print('Game over!')
						sett.game_active=False
			bullets[i+3].remove(bullet_hit)
	#敌机中弹
	for i in range(3):
		collisions0=pg.sprite.groupcollide(bullets[i],enemies,True,False)
		if collisions0:
			for bullet_hit,enemy_hit in collisions0.items():
				enemy_hit.life-=bullet_hit.lethality
				if enemy_hit.life<=0:
					enemies.remove(enemy_hit)

	#己方导弹中弹：
	for i in range(3):
		collisions1=pg.sprite.groupcollide(bullets[2],bullets[i+3],False,False)
		if collisions1:
			for mymissile,enmbullet in collisions1.items():			
				mymissile.life-=enmbullet.lethality
				if mymissile.life<=0:
					bullets[2].remove(mymissile)
				if i==2:
					enmbullet.life-=mymissile.lethality
					if enmbullet.life<=0:
						bullets[5].remove(enmbullet)
				else:
					bullets[i+3].remove(enmbullet)

	#对方导弹中弹
	for i in range(3):
		collisions2=pg.sprite.groupcollide(bullets[5],bullets[i],False,False)
		if collisions2:
			for enmmissile,mybullet in collisions2.items():			
				enmmissile.life-=mybullet.lethality
				if enmmissile.life<=0:
					bullets[5].remove(enmmissile)
				if i==2:
					mybullet.life-=enmmissile.lethality
					if mybullet.life<=0:
						bullets[2].remove(mybullet)
				else:
					bullets[i].remove(mybullet)