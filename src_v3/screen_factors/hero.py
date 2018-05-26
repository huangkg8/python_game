"""凯欢完成"""

import pygame as pg
import time

class Hero():
	def __init__(self, screen,sett):
		"""初始化hero并设置其初始位置"""
		self.screen = screen
		self.sett=sett
		# 加载hero图像并获取其外接矩形
		self.image = pg.image.load('image/Hero.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#初始位置（待改）
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		self.life=sett.hero_life
		self.speed=sett.hero_spped
		#hero占有的飞机或坦克,记得离开敌机时把它变为None
		self.plane=None	
		
		#射击方向（水平向右为0度，按d or c可以改变shoot_dir）
		self.shoot_dir=0

		#开导弹机时要轰炸的目标
		self.missile_target=None

		#移动标志
		self.moving_right = False
		self.moving_left = False
		self.moving_up=False  #攀爬
		self.jumping=False  #跳跃	
		self.falling=False  #自由落体（初速度为0）

	def drawme(self):
		"""在指定位置绘制hero"""
		if self.plane:
			pass
		else:
			self.screen.blit(self.image, self.rect)

	def update(self):
		if not self.plane:
			if self.moving_right:
				self.rect.centerx += self.speed
			elif self.moving_left:
				self.rect.centerx -= self.speed
			elif self.moving_up：
				self.rect.centery -= self.speed

			if self.jumping:
				#改变centery即可，当落地或跳上飞机时把self.jumping改为False，当碰到上界时变为自由落体运动（初速度为0）
				pass

		else:
			#判断是否超过驾驶时限
			if time.clock()>self.plane.jackedTime+self.plane.time_limit:
				#超时
				self.plane=None
				self.life-=1
				if self.life<=0:
					print('Game over')
					self.sett.game_active=False
			else:
				if self.plane.moving_right:
					self.plane.rect.centerx += self.plane.speed
				elif self.plane.moving_left:
					self.plane.rect.centerx -= self.plane.speed
				elif self.plane.moving_up：
					self.plane.rect.centery -= self.plane.speed
				elif self.plane.moving_down:
					self.plane.rect.centery += self.plane.speed

				#让hero.rect的位置与hero.plane.rect的位置保持一致
				self.rect.centerx,self.rect.centery=self.plane.rect.centerx,self.plane.rect.centery
