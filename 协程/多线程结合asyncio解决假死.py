import asyncio
import asyncio, time, threading

#需要执行的耗时异步任务
async def func(num):
    print(f'准备调用func,大约耗时{num}')
    await asyncio.sleep(num)
    print(f'耗时{num}之后,func函数运行结束')

#定义一个专门创建时间循环loop函数，在另一个线程中启动它
def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

#定义一个main函数
def main():
    coroutine1 = func(3)
    coroutine2 = func(2)
    coroutine3 = func(1)

    #在当前线程下创建时间循环，（未启用），在start_loop里面启动
    new_loop = asyncio.new_event_loop()
    #通过当前线程开启新的线程去启动时间循环
    t = threading.Thread(target = start_loop, args = (new_loop, ))
    #这几个是关键，代表在新线程中事件循环不断“游走”执行
    t.start()
    asyncio.run_coroutine_threadsafe(coroutine1, new_loop)
    asyncio.run_coroutine_threadsafe(coroutine2, new_loop)
    asyncio.run_coroutine_threadsafe(coroutine3, new_loop)

    for i in "iloveu":
        print(str(i) + "     ")
    
if __name__ == "__main__":
    main()




