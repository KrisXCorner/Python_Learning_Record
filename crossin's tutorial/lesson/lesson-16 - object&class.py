s = 'how are you'
l = s.split()

dir(s)
dir(l)

class MyClass:
    name = 'Sam'

    def sayHi(self):
        print('Hello %s'%self.name)     #类方法和我们之前定义的函数区别在于，第一个参数必须为self
    
mc = MyClass()  #类名加圆括号()的形式可以创建一个类的实例，也就是被称作对象的东西。我们把这个对象赋值给变量mc。于是，mc现在就是一个MyClass类的对象。
print(mc.name)
mc.name = 'Lily'
mc.sayHi()