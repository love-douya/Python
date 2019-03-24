import tkinter as tk
import time
import asyncio
import threading

class Form:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x300')
        self.root.title('窗体程序')

        self.button = tk.Button(self.root, text = "开始计算", command = self.change_form_state)
        self.label = tk.Label(master = self.root, text = "等待计算结果")

        self.button.pack()
        self.label.pack()
        
        self.root.mainloop()

    async def calculate(self):
        await asyncio.sleep(3)
        self.label["text"] = 300

    def get_loop(self, loop):
        self.loop = loop
        asyncio.set_event_loop(self.loop)
        self.loop.run_forever()

    def change_form_state(self):
        coroutine1 = self.calculate()
        #在当前线程下创建时间循环，（未启用），在start_loop里面启动它
        new_loop = asyncio.new_event_loop()
        #通过当前线程开启新的线程去启动时间循环
        t = threading.Thread(target = self.get_loop, args = (new_loop, ))
        t.start()
        #新线程中不断游走执行
        asyncio.run_coroutine_threadsafe(coroutine1, new_loop)

if __name__ == "__main__":
    form = Form()

    

    
