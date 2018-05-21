# python_game

类的设计

boss.py

    class Boss():
        def __init__(self, initpos):
       		"""
       		屏幕大小先设置为800 * 600
       		initpos: (x, y) 二个元素的元组
       		"""
    	def move(self, direction, dist):
            """
            direction: int;   值为0, 1, 2, 3(分别表示上下左右)
            dist: int  移动的距离
            """
        def attack(self, )

enemy.py

    class Enemy():
        def __init__(self, initpos, typed):
       		"""
       		屏幕大小先设置为800 * 600
       		initpos: (x, y) 二个元素的元组
       		typed: int,  (0: 飞机，1: 坦克)
       		需要初始化属性值
       		"""
    	def move(self, direction, dist):
            """
            direction: int;   值为0, 1, 2, 3(分别表示上下左右)
            dist: int  移动的距离
            """
        def attack(self, mode, direction):
            """
            mode: 攻击的模式(导弹，炮弹等)
            """
            

主角类

    class Hero():
        def __init__(self):
            """
            初始化属性值，包括初始位置
            """
        def move(self, direction, dist):
            """
            direction: int;   值为0, 1, 2, 3(分别表示上下左右)
            dist: int  移动的距离
            """
        def attack(self, mode, direction):
            """
            mode: 攻击的模式(导弹，炮弹等)
            """
            
        def upgrade(self, ):
            """
            升级，改变属性值
            """
    


