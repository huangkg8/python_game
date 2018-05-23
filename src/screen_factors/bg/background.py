"""
迪润完成
可自行拆分为多个文件
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

class Shop(Sprite):
	pass

#others,如地雷，各种食品或装备


class Background():
	def __init__(self):
		self.bg_factors=Group()
		#向bg_factors里面添加元素，也可以分多个编组