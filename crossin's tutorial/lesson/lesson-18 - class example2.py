class Vehicle:
    def __init__(self, speed):  # __init__函数会在类被创建的时候自动调用，用来初始化类。注意：__init__是python的内置方法，类似的函数名前后是两个下英文划线，如果写错了，则不会起到原本应有的作用。
        self.speed = speed
    def drive(self, distance):
        print('need %f hours'%(distance / self.speed))

class Bike(Vehicle):    # Bike(Vehicle)就是说Bike是「继承」自Vehicle中的子类。Vehicle中的属性和方法，Bike都会有
    pass

class Car(Vehicle):
    def __init__(self,speed,fuel):      # 重新定义了__init__和drive函数，这样会覆盖掉它继承自Vehicle的同名函数
        Vehicle.__init__(self,speed)    # 依然可以通过“Vehicle.函数名”来调用它的超类方法.因为是通过类名调用方法，所以这里必须提供self的参数值
        self.fuel = fuel

    def drive(self, distance):
        Vehicle.drive(self,distance)
        print('need %f fuels'%(distance * self.fuel)


b = Bike(15.0)
c = Car(80,0.012)
b.drive(100)
c.drive(100)
