import pymysql, os, time
from selenium import webdriver


class Support:

    driver = None       # 定义类变量driver，用于确保driver是单例

    def __init__(self):
        self.conn = pymysql.connect('localhost', 'root', '123456', 'woniusale', charset='utf8')
        self.cursor = self.conn.cursor()

    def query_one(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        return result

    def query_all(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def update_data(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except:
            return False
        else:
            return True

    # 实例化当前项目的driver，并确保只有一个实例(单例模式)
    @classmethod   # 类级方法，与类级变量一样，使用类名来调用，只会驻留在类空间里。
    def get_webdriver(cls, browser='firefox'):
        if cls.driver is None:
            if browser == 'ie':
                ie_driver = r"C:\Tools\IEDriverServer.exe"
                cls.driver = webdriver.Ie(executable_path=ie_driver)
            elif browser == 'chrome':
                chrome_driver = r"C:\Tools\chromedriver.exe"
                cls.driver = webdriver.Chrome(executable_path=chrome_driver)
            else:
                firefox_path = r"C:\Program Files (x86)\Mozilla Firefox 61\firefox.exe"
                driver_path = r"C:\Tools\geckodriver.exe"
                cls.driver = webdriver.Firefox(firefox_binary=firefox_path, executable_path=driver_path)

            cls.driver.maximize_window()
            cls.driver.set_page_load_timeout(10)  # 页面加载的超时时间
            cls.driver.set_script_timeout(10)  # 执行JavaScript脚本的超时时间
            cls.driver.implicitly_wait(10)  # 如果元素没有找到，尝试继续等待的时间

        return cls.driver


    # 从CSV文件中读取数据并返回一个[{}, {}]的数据格式，第一行必须为列名
    def read_csv(self, filename):
        file_path = os.path.abspath('.') + '/data/' + filename
        with open(file_path, mode='r') as file:
            content_list = file.readlines()

        print(content_list)
        # 拼装成一个列表+字典的数据格式并返回. 字符串的strip方法可以去除前后的不可见字符
        key1 = content_list[0].strip().split(',')[0]
        key2 = content_list[0].strip().split(',')[1]

        list = []
        for i in range(1, len(content_list)):
            dict = {}
            dict[key1] = content_list[i].strip().split(',')[0]
            dict[key2] = content_list[i].strip().split(',')[1]
            list.append(dict)

        return list

    # 保存测试结果
    # def write_result(self, content):
    #     filename = time.strftime('%Y%m%d_%H%M%S') + '.txt'
    #     file_path = os.path.abspath('.') + '/result/' + filename
    #     now = time.strftime('%Y-%m-%d %H:%M:%S\t')
    #     with open(file_path, mode='a+', encoding='utf-8') as file:
    #         file.write(now + content + '\n')

    def write_result(self, file_path, content):
        now = time.strftime('%Y-%m-%d %H:%M:%S\t')
        with open(file_path, mode='a+', encoding='utf-8') as file:
            file.write(now + content + '\n')

    # 截图，保留测试现场
    def capture_screen(self):
        filename = time.strftime('%Y%m%d_%H%M%S') + '.png'
        file_path = os.path.abspath('.') + '/screenshot/' + filename
        self.driver.get_screenshot_as_file(file_path)


    def __del__(self):
        self.conn.close()
        self.cursor.close()

if __name__ == '__main__':
    support = Support()
    support.read_csv('goods_info.csv')