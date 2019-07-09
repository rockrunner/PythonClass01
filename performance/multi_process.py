import multiprocessing
import threading
import time

count = 0

def test_1():
    for j in range(10):
        global count
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        print('%d: %s' % (count, now))
        count += 1
        time.sleep(1)


if __name__ == '__main__':
    for i in range(20):
        # threading.Thread(target=test_1).start()
        multiprocessing.Process(target=test_1).start()