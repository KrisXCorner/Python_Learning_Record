import pygame, random
from sys import exit

#定义一个Bullet类，封装子弹相关的数据和方法
class Bullet:
    def __init__(self):         #初始化成员变量，x，y，image
        self.x = 0
        self.y = -1
        self.image = pygame.image.load('./pygame/bullet.png').convert_alpha()    #子弹图像(透明图)
    
    def move(self):      #处理子弹的运动
        if self.y < 0:            
            mouse_x,mouse_y = pygame.mouse.get_pos()
            self.x = mouse_x - self.image.get_width()/2
            self.y = mouse_y - self.image.get_height()/2
        else:
            self.y -= 6

#为敌机创建一个类：Enemy
class Enemy:
    def restart(self):          # 重置敌机位置和速度
        self.x = random.randint(100,1100)
        self.y = random.randint(-200,-50)
        self.speed = random.random() + 0.5
    def __init__(self):
        self.restart()
        self.image = pygame.image.load('./pygame/UFO.png').convert_alpha()      #敌机图像
    def move(self):
        if self.y < 1280:
            self.y += self.speed        #向下移动
        else:
            self.restart()              #移动到屏幕下方就重置




pygame.init()       # 初始化pygame,为使用硬件做准备
screen = pygame.display.set_mode((1280,853),0,32)  # 创建了一个窗口,窗口大小和背景图片大小一样
pygame.display.set_caption("Hello world!")      # 设置窗口标题
background = pygame.image.load('./pygame/bg.jpg').convert()      #加载并转换图像
plane = pygame.image.load('./pygame/plane.png').convert_alpha()
bullet = Bullet()       # 创建一个 Bullet 实例
enemy = Enemy()

while True:             #游戏主循环
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()       #接收到退出事件后退出程序
            exit()
        
    screen.blit(background,(0,0))        #将背景图画上去
    bullet.move()           # 处理子弹运动
    screen.blit(bullet.image,(bullet.x,bullet.y))         #把子弹画到屏幕上
    
    x,y = pygame.mouse.get_pos()         #获取鼠标位置
    x -= plane.get_width()/2
    y -= plane.get_height()/2            #计算飞机的左上角位置
    screen.blit(plane,(x,y))             #把飞机画到屏幕上。图片加载顺序 由下到上 叠放

    enemy.move()                # 处理敌机运动
    screen.blit(enemy.image,(enemy.x,enemy.y))       #更新敌机位置

    pygame.display.update()              #刷新一下画面