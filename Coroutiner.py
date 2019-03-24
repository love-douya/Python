def consumer():
    r = ''
    while True:
        n = yield r #执行的中断点
        if not n:
            return
        print('[消费者]正在消费:{0}'.format(n))
        r = '200人名币'

def produce(c):
    #启动消费者（生成器）--实际上是函数调用，只不过生成器不是直接像函数那般调用的
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[生产者]正在生产:{0}'.format(n))
        r = c.send(n)#给消费者传入值--实际上也是函数调用
        print('[生产者]消费者返回:{0}'.format(r))
        print('---------------------------------')
    c.close()

c = consumer()
produce(c)