"""俊义完成"""

import pygame as pg
from pygame.sprite import Sprite
class Enemy(Sprite):
	def __init__(self,sett,life,speed,time_limit):
		super().__init__()
		self.sett=sett

		
		self.life=life #生命值
		self.speed=speed
		self.shoot_dir=180
		self.time_limit=time_limit #hero可以驾驶的时限 
		self.jackedTime=None #被劫机的时间

		self.moving_right=False
		self.moving_left=False
		self.moving_up=False
		self.moving_down=False

	def update(self):
		"""移动或发射子弹"""
		pass

	def drawme(self):
		pass


class Ordin_plane(Enemy):
	"""使用bullet0"""
	def __init__(self,sett):
		super().__init__(sett, sett.ordinPlaneLife, sett.ordinPlaneSpeed, sett.ordinPlaneTimeLimit)
		

class Multi_plane(Enemy):
	"""使用bullet1"""
	pass

class Missile_plane(Enemy):
	"""使用bullet2"""
	pass

class Tank(Enemy):
	
	pass