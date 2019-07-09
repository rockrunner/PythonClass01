import requests, time, random, threading, pymysql

class WoniuSalesTest:
    def __init__(self):
        self.session = requests.session()
        self.conn = pymysql.connect('192.168.49.129', 'root', '123456', 'woniusales', charset='utf8')
        self.cursor = self.conn.cursor()

    def do_login(self):
        data = {'username': 'admin', 'password': 'admin123', 'verifycode': '0000'}
        resp = self.session.post('http://192.168.49.129:8080/woniusales/user/login', data=data)
        if resp.text == 'login-pass':
            print("登录成功.")
        else:
            print('登录失败.')

    def add_customer(self):
        customer_phone = random.randrange(10000000, 99999999)
        data = {'customername':'PyUser','customerphone':'138%d' % customer_phone,'childsex':'男',
                'childdate':'2017-12-10','creditkids':'200','creditcloth':'150'}
        resp = self.session.post(url='http://192.168.49.129:8080/woniusales/customer/add', data=data)
        if resp.text == 'add-successful':
            print("新增客户成功.")
        else:
            print("新增客户失败.")

    # 构建一个性能测试基础脚本
    def main_test(self):
        for i in range(20):
            self.do_login()
            self.add_customer()
            time.sleep(1)


    # 利用多线程技术往数据库插入数据
    def insert_data(self):
        for i in range(20):   # 20次iteration迭代
            customer_phone = random.randrange(10000000, 99999999)
            now = time.strftime('%Y-%m-%d %H:%M:%S')
            sql = "insert into customer(customername, customerphone, childsex, childdate, creditkids, creditcloth, credittotal, userid, createtime, updatetime) " \
                  "values('性能测试', '138%d', '男', '2017-9-10', 200, 100, 300, 3, '%s', '%s')" % (customer_phone, now, now)
            print(sql)
            self.cursor.execute(sql)
            self.conn.commit()
            time.sleep(1)


if __name__ == '__main__':
    wst = WoniuSalesTest()
    for i in range(100):      # 50个thread并发
        threading.Thread(target=wst.main_test).start()
        # threading.Thread(target=wst.insert_data).start()
