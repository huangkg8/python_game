"""欢欢完成"""

import pygame as pg
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""父类"""
	def __init__(self,sett,screen,shooter,byhero, _type):
		super().__init__()	
		self.sett=sett
		self.screen=screen
		self.screen_rect = screen.get_rect()
		self.shooter=shooter #发射子弹的对象	
		self.byhero=byhero #标记该子弹是不是hero发射的(True or False)

		#导入子弹图像
		if _type==0:
			graph='image/bullet0.bmp'
		elif _type==1:
			graph='image/bullet1.bmp'
		elif _type==2:
			graph='image/bullet2.bmp'
		self.image = pg.image.load(graph)
		self.rect = self.image.get_rect()
		
		#根据shooter（同样有属性rect）位置初始化子弹位置
		
		#存储用小数表示的子弹位置
		
	def drawme(self):
		pass

class Bullet0(Bullet):
	"""普通子弹,直线飞行"""
	def __init__(self, sett, screen, shooter,dir,byhero):
		"""在发射点所处的位置创建一个子弹对象"""
		super().__init__(sett,screen,shooter,byhero,0)
		self.dir=dir  #子弹方向

	def update(self):
		#更新子弹位置
		pass
		
	
class Bullet1(Bullet):
	"""多核弹，直线飞到一定距离后分裂"""
	def __init__(self, sett, screen, shooter,dir,byhero):
		"""在发射点所处的位置创建一个子弹对象"""
		super().__init__(sett,screen,shooter,byhero,1)
		self.dir=dir
	
	def update(self,bullets):
		#更新子弹位置，分裂后生成几个Bullet0,保存进编组bullets[0 or 3],并在bullets[1 or 4]中销毁该Bullet1
		pass		

	
class Bullet2(Bullet):
	"""导弹，能一直追踪hero，能被子弹击落"""
	def __init__(self,sett,screen,shooter,target,byhero):
		super().__init__(sett,screen,shooter,byhero,2)
		self.life=sett.bullet2_life #导弹生命值
		self.target=target #导弹目标
		
	def update(self):
		"""
		每次更新位置都朝着target_pos方向即可
		"""
		target_pos=(self.target.rect.centerx, self.target.rect.centery)

		#snip