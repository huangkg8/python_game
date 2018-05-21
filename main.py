import pygame
import sys
from bg.shop import *

def run_game():
    #初始化窗口大小和标题
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("hello")

    #事件处理函数
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()

run_game()

