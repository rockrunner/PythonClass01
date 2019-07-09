'''
WoniuSales性能测试思路分析： 测试登录
1. 用协议实现请求: requests。
2. 多线程处理: threading。
- 加上线程名
- 每个线程执行多次
3.脚本优化
- 维护cookie
    a.登录后取响应中的set-cookie字段，提供给后面的方法用。
    b.session()方法：保持session。构造方法。
- 检查点（断言）
    处理json数据
4. 监控业务指标：响应时间、TPS
- 响应时间： time
- TPS：事务数和时间
5. 监控系统指标：CPU、Memory、Disk。
- pip install psutil
6. 如何处理数据
- 封装一个功能，写文件的功能
- 每个数据都调用这个功能，写入不同的文件
- 用excel生成图表
'''
import requests,time,threading,json,psutil

class PerformanceTest:
    # 创建对象时，得到session，后面的操作全部使用这个session对象去发送请求。
    def __init__(self):
        self.session = requests.session()
        self.count = 0
        self.startTime = round(time.time() * 1000)

    def doLogin(self):
        # 得到当前时间
        start = round(time.time() * 1000)
        loginData = {'username':'admin','password':'Milor123','verifycode':'0000'}
        response = self.session.post("http://localhost:8088/woniusales/user/login",data=loginData)
        # print(response.text)
        print("当前线程名为：%s"%(threading.current_thread().getName()))
        self.assertIt('login-pass',response.text)
        # 得到当前时间
        end = round(time.time() * 1000)
        # 输出end减去start的时间
        print('登录的响应时间为%d ms!'%(end-start))

    def doCheck(self):
        start = round(time.time() * 1000)
        postData = {'goodsserial':'','goodsname':'','barcode':'','goodstype':'','earlystoretime':'','laststoretime':'','page':'1'}
        response = self.session.post("http://localhost:8088/woniusales/query/stored",data=postData)
        print("当前线程名为：%s"%(threading.current_thread().getName()))
        # self.assertIt('goodsserial',response.text)
        # 将响应的json数据转换成python中的内置数据类型list,再转换成str
        data = str(json.loads(response.text))
        self.assertIt('goodsserial',data)
        # 得到当前时间
        end = round(time.time() * 1000)
        # 输出end减去start的时间
        print('库存查询的响应时间为%d ms!'%(end-start))

    def assertIt(self,expected, actual):
        if expected in actual:
            print("Pass.")
        else:
            print("Fail.")

    def start(self,count):
        # 循环执行多次doLogin
        for i in range(count):
            self.doLogin()
            self.count += 1
            self.doCheck()
            self.count += 1

    def monitor(self):
        print('CPU使用率  内存使用率  C盘使用率  进程数')
        while (True):
            # 得到cpu、内存、磁盘、进程的数据
            cpu = psutil.cpu_percent()
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage("c:\\")
            process = psutil.pids()
            print(str(cpu) + '%      ' + str(memory.percent) + '%      '\
                  + str(disk.percent) + '%      ' + str(len(process)))
            time.sleep(3)


    def getResult(self):
        endTime = round(time.time() * 1000)
        print('事务总数为：%d'%(self.count))
        print('运行时间为：%d ms'%(endTime - self.startTime))
        print('TPS为：%f'%(self.count / ((endTime - self.startTime) / 1000)))

if __name__  == '__main__':
    # 实例化
    p = PerformanceTest()
    # 调用监控的方法： 让监控和性能测试同时执行，专门启动一个线程处理监控
    # p.monitor()
    threading.Thread(target=p.monitor).start()
    # 创建一个列表保存所有线程
    threadList = []
    for i in range(5):
        t = threading.Thread(target=p.start,args=(5,))
        # 把线程对象保存到列表中去
        threadList.append(t)
        t.start()

    for thread in threadList:
        # 让主线程在所有子线程运行完后再执行，用到join方法
        # 造成主线程阻塞
        thread.join()

    p.getResult()