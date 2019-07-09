import threading, time

# 直接定义一个类，并继承threading.Thread类，并重新父类方法run。
# class ThreadDemo(threading.Thread):
#
#     # 重写父类方法，以完成多线程调用
#     def run(self):
#         time.sleep(1)
#         now = time.strftime('%Y-%m-%d %H:%M:%S')    # 线程的运行，完全是运气，没有规律，不按顺序，无法通过代码控制。
#         print(self.name + ': ' + now)
#
#
# if __name__ == '__main__':
#     print("开始搬砖...")
#     for i in range(10):
#         demo = ThreadDemo()
#         # demo.run()      # 正常地调用一个普通类的方法而已。
#         demo.start()      # 每一次循环，新建一个线程来运行，进而达到10个线程同时并发运行的效果。
#     print("搬砖结束...")



# 直接实例化threading.Thread类，并传递要进行多线程运行的函数或方法以及对应的参数（常用）。
def print_one(x, y):
    for i in range(20):
        time.sleep(1)
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        print(threading.current_thread().name + ': ' + now)

def print_two():
    time.sleep(1)
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    print(threading.current_thread().name + ': ' + now)

thread_list = []
for i in range(20):
    # threading.Thread(target=print_one, args=(100,200)).start()
    t = threading.Thread(target=print_two)     # 通过在实例化Thread类时，传递构造参数完成多线程处理。
    thread_list.append(t)


# for t in thread_list:
#     t.start()        # 将子线程合并到主线程，进而实现主线程一定要等待着所有子线程结束后，才能结束自己。
#     if t.name == 'Thread-10':
#         t.join()


for t in thread_list:
    t.setDaemon(True)   # 放在start()之前，将该线程设置为守护线程，一旦主线程结束，子线程将无机会运行。
    t.start()


time.sleep(0.999)
print("当前线程名为：" + threading.current_thread().getName())
