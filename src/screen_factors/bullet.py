"""欢欢完成"""

import pygame as pg
from pygame.sprite import Sprite

class Bullet0(Sprite):
	"""普通子弹"""
	def __init__(self, sett, screen, shooter,dir,byhero):
		"""在发射点所处的位置创建一个子弹对象"""
		super().__init__()
		self.screen = screen

		#导入子弹图像
		self.image = pg.image.load('images/bullet0.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#初始化子弹位置
		

		#存储用小数表示的子弹位置
		

		#速度与方向
		self.speed = sett.bullet0_speed
		self.dir=dir  #子弹方向

		#标记该子弹是不是hero发射的(True or False)
		self.byhero=byhero
	
		

	def update(self):
		#更新子弹位置
		pass
		
	def drawme(self):
		#绘制子弹
		pass

class Bullet1(Sprite):
	"""多核弹，飞到一定距离后分裂"""
	def __init__(self, sett, screen, shooter,dir,byhero):
		"""在发射点所处的位置创建一个子弹对象"""
		pass
	
	def update(self,bullets):
		#更新子弹位置，分裂后生成几个Bullet0,保存进编组bullets[0 or 3],并在bullets[1 or 4]中销毁该Bullet1
		pass		

	def drawme(self):
		#绘制子弹
		pass


class Bullet2(Sprite):
	"""导弹，能一直追踪hero，能被子弹击落"""
	def __init__(self,sett,screen,shooter,byhero,target):
		self.life=sett.bullet2_life

		#如果是hero发射的子弹,则要根据self.target（一个enermy类对象）来导航
		self.target=target
		pass

	def update(self):
		"""
		hero_pos是记录目标位置的元组（x,y）
		如果byhero==False，则根据hero_pos来导航
		如果byhero==True,则根据(self.target.rect.centerx,self.target.rect.centery)来导航		

		"""
		target_pos=(self.target.rect.centerx,self.target.rect.centery)

		#snip