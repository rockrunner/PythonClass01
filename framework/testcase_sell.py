from selenium import webdriver
import time, random

from selenium.webdriver.common.keys import Keys

from framework.support import Support


class TestSell:
    def __init__(self, brower, support):
        self.driver = Support.get_webdriver(brower)
        self.support = support

    def main_test(self):
        self.prepare()
        self.barcode()
        self.customer_random()
        self.null_1()

    def prepare(self):
        self.driver.find_element_by_link_text('销售出库').click()
        time.sleep(2)

    def barcode(self):
        barcode_list = self.support.read_csv('goods_info.csv')
        for i in range(len(barcode_list)):
            # random_index = random.randrange(0, len(barcode_list))
            self.driver.find_element_by_id("barcode").clear()
            # self.driver.find_element_by_id("barcode").send_keys(barcode_list[random_index]['barcode'])
            self.driver.find_element_by_id("barcode").send_keys(barcode_list[i]['barcode'])
            self.driver.find_element_by_xpath("(//button[@type='button'])[5]").click()
            time.sleep(2)

            # 从数据库中获取对应的条码的价格，并和页面上的显示的价格进行对比，实现断言
            unitprice = self.db.query_one("select unitprice from goods where barcode='%s'" % barcode_list[i])[0]
            # 从折扣比例的文本框中获取其值，不能使用.text，而必须获取其value属性
            discount_ratio = self.driver.find_element_by_css_selector("td.discountratio > input[type='text']").get_attribute('value')

            if unitprice * int(discount_ratio) / 100 == float(self.driver.find_element_by_id('tempbuyprice').text):
                print("扫码成功.")
            else:
                print('扫码失败.')


    def customer_random(self):
        self.driver.find_element_by_id('customerphone').send_keys('18')
        random_count = random.randrange(1, 10)
        for i in range(random_count):
            self.driver.find_element_by_id('customerphone').send_keys(Keys.ARROW_DOWN)
            time.sleep(0.5)
        self.driver.find_element_by_id('customerphone').send_keys(Keys.ENTER)
        time.sleep(3)

    def null_1(self):
        pass