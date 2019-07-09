import http.client, time, random
from framework.support import Support

class WoniuSalesThree:
    def __init__(self):
        self.host = 'localhost'
        self.port = 8088
        self.cookie = ''
        self.support = Support()

    def __del__(self):
        pass

    def test_login(self):
        conn = http.client.HTTPConnection(host=self.host, port=self.port)
        param = 'username=admin&password=admin123&verifycode=0000'
        # 只是要POST请求带文本型k=v&k=v&k=v，必须设置content-type=application/x-www-form-urlencoded
        # 如果是利用POST请求上传文件，必须设置content-type=multipart/form-data
        header = {'Content-Type': 'application/x-www-form-urlencoded', 'Cookie':'9527'}
        conn.request(method="POST", url='/woniusales/user/login', body=param, headers=header)
        resp = conn.getresponse()
        # print(resp.getheaders())  # 获取当前响应头的所有字段的值

        # self.cookie = resp.getheader('Set-Cookie')    # 获取响应头的指定字段的值
        # print(self.cookie)

        cookie_list = resp.getheaders()
        # print(cookie_list)
        for mycookie in cookie_list:
            if mycookie[0] == 'Set-Cookie':
                cookie_value = str(mycookie[1]).split(';')[0]
                self.cookie = self.cookie + cookie_value + ';'


    # 打开会员管理首页
    def test_customer_home(self):
        conn = http.client.HTTPConnection(host=self.host, port=self.port)
        header = {'Cookie': self.cookie}
        conn.request(method='GET', url='/woniusales/customer', headers=header)
        resp = conn.getresponse()
        content = resp.read().decode()
        # print(content)
        if '蜗牛进销存-会员管理' in content:
            print("打开会员管理首页成功.")
        else:
            print("打开会员管理首页失败.")

    # 会员的新增
    def test_customer_add(self):
        conn = http.client.HTTPConnection(host=self.host, port=self.port)
        header = {'Content-Type': 'application/x-www-form-urlencoded', 'Cookie': self.cookie}
        customer_phone = random.randrange(10000000, 99999999)
        data = 'customername=接口测试&customerphone=138%d&childsex=男&childdate=2017-12-10&creditkids=200&creditcloth=150' % customer_phone
        conn.request(method='POST', url='/woniusales/customer/add', body=data.encode(), headers=header)
        resp = conn.getresponse()

        query_result = self.support.query_one("select customerphone from customer where customerphone='%s%s'" % ('138', customer_phone))
        if resp.read().decode() == 'add-successful' and query_result[0] == '138%s' % customer_phone:
            print("新增客户数据成功.")
        else:
            print("新增客户数据失败.")


    # 会员的修改：不登录也可处理，是BUG
    def test_customer_edit(self):
        # 修改之前，先随机获取到一条客户信息
        query_customer = self.support.query_one('select customerid, customerphone, customername, childsex, childdate, creditkids, creditcloth'
                                             ' from customer order by RAND() limit 0, 1')
        # print(query_customer)
        customer_id = query_customer[0]
        customer_phone = query_customer[1]
        customer_name = '接口修改'
        child_sex = query_customer[3]
        child_date = query_customer[4]
        credit_kids = query_customer[5]
        credit_cloth = query_customer[6]

        data = 'customerid=%d&customerphone=%s&customername=%s&childsex=%s&childdate=%s&creditkids=%d&creditcloth=%d' % (
            customer_id, customer_phone, customer_name, child_sex, child_date, credit_kids, credit_cloth
        )
        conn = http.client.HTTPConnection(host=self.host, port=self.port)
        header = {'Content-Type': 'application/x-www-form-urlencoded', 'Cookie': self.cookie}
        conn.request(method='POST', url='/woniusales/customer/edit', body=data.encode(), headers=header)
        resp = conn.getresponse()
        # print(resp.read().decode())

        query_name =self.support.query_one("select customername from customer where customerphone='%s'" % customer_phone)
        if resp.read().decode() == 'edit-successful' and query_name[0] == '接口修改':
            print("修改编号为[%d]的客户信息成功." % customer_id)
        else:
            print("修改编号为[%d]的客户信息失败." % customer_id)


    # 会员查询：不登录也可处理，是BUG
    def test_customer_search(self):
        conn = http.client.HTTPConnection(host=self.host, port=self.port)
        header = {'Content-Type': 'application/x-www-form-urlencoded', 'Cookie': self.cookie}
        data = 'customerphone=&page=1'
        conn.request(method='POST', url='/woniusales/customer/search', body=data, headers=header)
        resp = conn.getresponse()
        content = resp.read().decode()
        print(type(content))
        print(content)



if __name__ == '__main__':
    three = WoniuSalesThree()
    # three.test_login()
    # three.test_customer_home()
    # three.test_customer_add()
    # three.test_customer_edit()
    three.test_customer_search()