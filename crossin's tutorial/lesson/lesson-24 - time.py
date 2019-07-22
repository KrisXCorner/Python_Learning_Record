import time

starttime = time.time()
print('start:%f'%starttime)

for i in range(1,10):
    print(i)

endtime = time.time()
print(endtime)
print('total time:%f'%(endtime - starttime))


print(1)
time.sleep(3)   # 让程序暂停secs秒
print(2)

# 在抓取网页的时候，适当让程序sleep一下，可以减少短时间内的请求，提高请求的成功率