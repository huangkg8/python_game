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
		self.x=float(self.rect.centerx)
		self.y=float(self.rect.centery)

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
		self.jumporfall=False  #跳跃或下落	
		self.jumpfallspeed=0  #在空中的竖直速度
		self.jump_init_speed=sett.jump_init_speed #起跳时的竖直速度

	def drawme(self):
		"""在指定位置绘制hero"""
		if self.plane:
			self.screen.blit(self.plane.image, self.rect)
		else:
			self.screen.blit(self.image, self.rect)

	def update(self):
		if not self.plane:
			if self.moving_right:
				self.x += self.speed
				self.rect.centerx=self.x

			elif self.moving_left:
				self.x -= self.speed
				self.rect.centerx=self.x

			elif self.moving_up： #攀爬
				self.y -= self.speed
				self.rect.centery=self.y

			if self.jumporfall:
				self.y+=self.jumpfallspeed
				self.jumpfallspeed+=self.sett.acc
				self.rect.centery=self.y				
				#碰到上界反弹
				if self.rect.centery<=0:
					self.jumpfallspeed = -self.jumpfallspeed
				#落地后停止下落
				elif self.rect.centery>=self.sett.groundy: 
					self.jumporfall=False


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
					self.plane.x += self.plane.speed
					self.plane.rect.centerx =self.plane.x
				elif self.plane.moving_left:
					self.plane.x -= self.plane.speed
					self.plane.rect.centerx =self.plane.x
				elif self.plane.moving_up：
					self.plane.y -= self.plane.speed
					self.plane.rect.centery =self.plane.y
				elif self.plane.moving_down:
					self.plane.y += self.plane.speed
					self.plane.rect.centery = self.plane.y

				#让hero.rect的位置与hero.plane.rect的位置保持一致
				self.rect.centerx, self.rect.centery = self.plane.rect.centerx, self.plane.rect.centery
