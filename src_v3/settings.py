import pygame as pg

class Settings():
	"""存储游戏中的所有设置,比如屏幕属性，速度，生命值"""
	def __init__(self):
		
		self.game_active=True

		#屏幕设置
		self.screen_width=1200
		self.screen_height=800
		self.bg_color=(220,220,220)

		#子弹设置
		self.dir_factor=18  #方向改变单位(即每按一下改变多少度数)
		self.lethality=[1,3,2] #子弹杀伤力
		
		self.bullet0_speed = 2
		self.bullet1_speed = 2
		self.bullet2_speed = 3

		self.bullet2_life=3
		

		#hero设置
		self.hero_life=5
		self.hero_speed=3


		#enemies设置
		self.ordinPlaneLife=2
		self.multiPlaneLife=3
		self.missilePlaneLife=3
		self.tankLife=5

		self.ordinPlaneSpeed=2
		self.multiPlaneSpeed=2
		self.missilePlaneSpeed=2

		self.ordinPlaneTimeLimit=120
		self.multiPlaneTimeLimit=90
		self.missilePlaneTimeLimit=50
		self.tankTimeLimit=120
		#other settings
	
	