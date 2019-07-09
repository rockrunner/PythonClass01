from pykeyboard import PyKeyboard
from pymouse import PyMouse
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time, os, random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from webui.database import DataBase


class WoniuSalesThree:
    def __init__(self):

        # 做一个初始化工作，定义本类需要用到的实例变量
        self.keyboard = PyKeyboard()
        self.db = DataBase()

        # 手工指定Firefox的路径和Driver的路径:
        firefox_path = r"C:\Program Files (x86)\Mozilla Firefox 61\firefox.exe"
        driver_path = r"C:\Tools\geckodriver.exe"
        # 打开浏览器，启动GeckoDriver应用程序
        self.driver = webdriver.Firefox(firefox_binary=firefox_path, executable_path=driver_path)

        # 让浏览器最大化
        self.driver.maximize_window()
        # 设置等待的超时时间
        self.driver.set_page_load_timeout(10)    # 页面加载的超时时间
        self.driver.set_script_timeout(10)       # 执行JavaScript脚本的超时时间
        self.driver.implicitly_wait(10)         # 如果元素没有找到，尝试继续等待的时间

        self.driver.get("http://localhost:8088/woniusales/")

    def login(self):
        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys("admin")
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys("admin123")
        self.driver.find_element_by_id("verifycode").clear()
        self.driver.find_element_by_id("verifycode").send_keys("0000")
        self.driver.find_element_by_css_selector("button.form-control.btn-primary").click()

        if self.is_element_present(By.LINK_TEXT, u"注销"):
            print("登录成功.")
        else:
            print("登录失败.")


    # 输入不同的商品条码进行处理
    def sell_barcode_1(self):
        barcode_list = ['6955203659590', '6955203645890', '6955203651099', '6955203655011', '6955203660213']
        # [{'barcode':'1111', 'price':100, 'quantity':6}, {}, {}]
        random_index = random.randrange(0, len(barcode_list))
        self.driver.find_element_by_id("barcode").clear()
        self.driver.find_element_by_id("barcode").send_keys(barcode_list[random_index])
        self.driver.find_element_by_xpath("(//button[@type='button'])[5]").click()
        time.sleep(2)

        # 从数据库中获取对应的条码的价格，并和页面上的显示的价格进行对比，实现断言
        unitprice = self.db.query_one("select unitprice from goods where barcode='%s'" % barcode_list[random_index])[0]
        # 从折扣比例的文本框中获取其值，不能使用.text，而必须获取其value属性
        discount_ratio = self.driver.find_element_by_css_selector("td.discountratio > input[type='text']").get_attribute('value')
        # "//tbody[@id='goodslist']/tr[3]/td[6]/input"  "//tbody[@id='goodslist']/tr[2]/td[6]/input"

        if unitprice*int(discount_ratio)/100 == float(self.driver.find_element_by_id('tempbuyprice').text):
            print("扫码成功.")
        else:
            print('扫码失败.')

    # 从数据库中直接随机取一条或多条商品条码进行处理
    def sell_barcode_2(self):
        sql = "SELECT barcode, unitprice FROM goods where barcode <> '0' ORDER BY RAND() LIMIT 1"
        barcode, unitprice = self.db.query_one(sql)
        self.driver.find_element_by_id("barcode").clear()
        self.driver.find_element_by_id("barcode").send_keys(barcode)
        self.driver.find_element_by_xpath("(//button[@type='button'])[5]").click()
        time.sleep(2)

        discount_ratio = self.driver.find_element_by_css_selector("td.discountratio > input[type='text']").get_attribute('value')
        if unitprice*int(discount_ratio)/100 == float(self.driver.find_element_by_id('tempbuyprice').text):
            print("扫码成功.")
        else:
            print('扫码失败.')


    # 随机挑选会员进行商品购买
    def customer_random_buy(self):
        # 第一种方式：从数据库中随机挑一条用户的电话号码。
        # 第二种方式：输入18，从自动完成的下拉列表中随机选一个。
        self.driver.find_element_by_id('customerphone').send_keys('18')
        random_count = random.randrange(1, 10)
        for i in range(random_count):
            self.driver.find_element_by_id('customerphone').send_keys(Keys.ARROW_DOWN)
            time.sleep(0.5)
        self.driver.find_element_by_id('customerphone').send_keys(Keys.ENTER)
        time.sleep(3)


    # 批次文件上传
    def batch_upload(self):
        self.driver.find_element_by_link_text("批次管理").click()
        time.sleep(3)
        # self.driver.find_element_by_id('batchfile').send_keys("D:\\Other\\销售出库单-20171020-Test.xls")
        # self.driver.find_element_by_xpath("//form[@class='form-inline']/div/input").click()

        ActionChains(self.driver).click(self.driver.find_element_by_id('batchfile')).perform()
        time.sleep(3)

        # 使用PyUserInput库：PyMouse和PyKeyboard，请先安排pyHook和PyUserInput
        keyboard = self.keyboard
        keyboard.type_string(r"D:\Other\SaleList-20171020-Test.xls")   # 往鼠标的焦点处输入一段字符串
        time.sleep(3)
        keyboard.press_key(keyboard.enter_key)
        keyboard.release_key(keyboard.enter_key)

        time.sleep(5)
        self.driver.find_element_by_xpath("//form[@class='form-inline']/div/input").click()

    # 批次管理：修改，删除
    def batch_manage(self):
        self.driver.find_element_by_link_text("批次管理").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@value='确认查询']").click()
        time.sleep(2)
        data = self.driver.find_element_by_xpath("//tbody[@id='batchinfo']/tr[3]/td[5]").text
        print(data)

        # 随机删除一条数据
        # 取整个表格的text值，并根据\n进行split并返回一个列表，求列表的长度
        # batch_data = self.driver.find_element_by_id('batchinfo').text

        # 取得当前表格中的最后一行的第一列的编号值，即为其数量
        # max_count = self.driver.find_element_by_css_selector("#batchinfo > tr:last-child > td").text

        # 根据xpath对tbody下面的所有tr进行获取，并计算其长度
        tr_list = self.driver.find_elements_by_xpath("//tbody[@id='batchinfo']/tr")

        random_index = random.randrange(0, len(tr_list))  # 不能写死，如何只有10条怎么办? 灵活求长度
        # 删除之前获取到随机选中的这一行的统一编号，供后续去数据库查询
        id = self.driver.find_element_by_xpath("//tbody[@id='batchinfo']/tr[%d]/td[2]" % random_index).text

        self.driver.find_element_by_xpath("(//a[contains(text(),'删除')])[%d]" % random_index).click()
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        self.keyboard.press_key(self.keyboard.enter_key)
        self.keyboard.release_key(self.keyboard.enter_key)
        # 如何断言？怎么判断该条记录已经被删除，注意：删除前是随机选择的一条。
        tr_after = self.driver.find_elements_by_xpath("//tbody[@id='batchinfo']/tr")
        length_check = (len(tr_list) - 1) == len(tr_after)
        id_check = self.db.query_one("select * from goods where goodsid=%d" % int(id)) is None

        if length_check and id_check:
            print("删除成功.")
        else:
            print("删除失败.")


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except:
            return False
        else:
            return True


    def __del__(self):
        # self.driver.quit()
        pass


if __name__ == '__main__':
    wst = WoniuSalesThree()
    wst.login()
    # wst.sell_barcode_2()
    # wst.customer_random_buy()
    wst.batch_manage()