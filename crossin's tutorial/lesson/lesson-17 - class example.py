class Car:
    speed = 0
    def drive(self, distance):
        time = distance / self.speed
        print(time)

car1 = Car()
car1.speed = 60
car1.drive(100)
car1.drive(200)

car2 = Car()
car2.speed = 150
car2.drive(100)
car2.drive(200)


#面向过程把数据和处理数据的计算全部放在一起，当功能复杂之后，就会显得很混乱，且容易产生很多重复的代码。
#而面向对象，把一类数据和处理这类数据的方法封装在一个类中，让程序的结构更清晰，不同的功能之间相互独立。
#这样更有利于进行模块化的开发方式。