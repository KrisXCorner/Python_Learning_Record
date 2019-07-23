import pygame
from sys import exit

pygame.init()       # 初始化pygame,为使用硬件做准备
screen = pygame.display.set_mode((1280,853),0,32)  # 创建了一个窗口,窗口大小和背景图片大小一样
pygame.display.set_caption("Hello world!")      # 设置窗口标题
background = pygame.image.load('./pygame/bg.jpg').convert()      #加载并转换图像
background_2 = pygame.image.load('./pygame/bg2.jpeg').convert()     #点击后的图像

while True:             #游戏主循环
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()       #接收到退出事件后退出程序
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:        #接收到鼠标按下事件后更换背景
            background = background_2
    screen.blit(background,(0,0))        #将背景图画上去
    pygame.display.update()              #刷新一下画面