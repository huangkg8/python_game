"""俊义完成"""

import pygame as pg

class Hero():
	def __init__(self, screen,sett):
		"""初始化hero并设置其初始位置"""

		self.screen = screen

		# 加载hero图像并获取其外接矩形
		self.image = pg.image.load('images/Hero.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#初始位置（待改）
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		#hero占有的飞机或坦克,记得离开敌机时把它变为None
		self.plane=None	
		
		#开导弹机时要轰炸的目标
		self.missile_target=None

		#移动标志
		self.moving_right = False
		self.moving_left = False
		self.moving_up=False  #攀爬
		self.jumping=False	

		self.sett=sett

	def drawme(self):
		"""在指定位置绘制hero"""
		if self.plane:
			pass
		else:
			self.screen.blit(self.image, self.rect)

	def update(self):
		if self.plane:
			pass

		else:
			if self.moving_right:
				self.rect.centerx += 1
			elif self.moving_left:
				self.rect.centerx -= 1
			elif self.moving_up：
				self.rect.centery-=1

			if self.jumping:
				#改变centery即可，当落地时把self.jumping改为False
				pass

			#snip
