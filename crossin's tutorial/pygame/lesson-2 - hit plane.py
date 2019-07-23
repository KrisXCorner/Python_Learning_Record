import pygame
from sys import exit

pygame.init()       # 初始化pygame,为使用硬件做准备
screen = pygame.display.set_mode((1280,853),0,32)  # 创建了一个窗口,窗口大小和背景图片大小一样
pygame.display.set_caption("Hello world!")      # 设置窗口标题
background = pygame.image.load('./pygame/bg.jpg').convert()      #加载并转换图像
bullet = pygame.image.load('./pygame/bullet.png').convert_alpha()     #点击后的图像(透明图)
plane = pygame.image.load('./pygame/plane.png').convert_alpha()
bullet_x = 0
bullet_y = -1

while True:             #游戏主循环
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()       #接收到退出事件后退出程序
            exit()
        
    screen.blit(background,(0,0))        #将背景图画上去
    x,y = pygame.mouse.get_pos()         #获取鼠标位置
    if bullet_y < 0:            #如果子弹位置超出了屏幕上端
        bullet_x = x - bullet.get_width()/2
        bullet_y = y - bullet.get_height()/2        #把子弹的中心位置设为鼠标坐标
    else:
        bullet_y -= 5            #子弹的位置往上移(模拟子弹发射出去轨迹)
    screen.blit(bullet,(bullet_x,bullet_y))         #把子弹画到屏幕上
    
    x -= plane.get_width()/2
    y -= plane.get_height()/2            #计算飞机的左上角位置
    screen.blit(plane,(x,y))             #把飞机画到屏幕上。图片加载顺序 由下到上 叠放
    pygame.display.update()              #刷新一下画面