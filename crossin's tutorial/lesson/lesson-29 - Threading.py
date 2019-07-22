# python 里有一个 threading 模块，其中提供了一个函数：
# threading.Thread(target=function, args=(), kwargs={})
# 
# function 是开发者定义的线程函数，
# args 是传递给线程函数的参数，必须是tuple类型，
# kwargs 是可选参数，字典类型。
# 
# 调用 threading.Thread 之后，会创建一个新的线程，参数 target 指定线程将要运行的函数，args 和 kwargs 则指定函数的参数来执行 function 函数。


import requests,threading

def get_weather(city):
    req = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=%s'%city)
    dic_city = req.json()

    city_data = dic_city.get('data')
    print(city_data.get('city'))

    if city_data:
        city_forecast = city_data['forecast'][0]  # 下面的都可以换成'get'方法
        print(city_forecast.get('date'))
        print(city_forecast.get('high'))
        print(city_forecast.get('low'))
        print(city_forecast.get('type'))
    else:
        print('未获得')
    print()

threads = []
cities = ['北京', '南京', '上海', '深圳', '广州', '杭州', '苏州', '天津', '西安', '成都']
files = range(len(cities))
for i in files:     # 创建线程
    t = threading.Thread(target=get_weather,args=(cities[i],))  # args 是传递给线程函数的参数，必须是tuple类型
    threads.append(t)
for i in files:     # 在第二个循环中，start 正式开启子线程；
    threads[i].start()
for i in files:     # 在第三个循环中，join 用来同步数据，主线程运行到这一步，将会停下来等待子线程运行完毕。没有这句，主线程则会忽略子线程，运行完自己的代码后结束程序。
    threads[i].join()
print('获取结束')