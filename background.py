"""
各种场景元素的类
"""

import pygame as pg
from pygame.sprite import Group
from pygame.sprite import Sprite

class Tree(Sprite):
	pass

class Springboard(Sprite):
	pass

class Trench(Sprite):
	pass

#others,如地雷，各种食品或装备

class Background():
	"""总类"""
	def __init__(self):
		self.bg_factors=Group()
		#向bg_factors里面添加各种场景元素，也可以分多个编组
