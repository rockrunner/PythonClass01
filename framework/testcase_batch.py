from selenium import webdriver
import time

from selenium.webdriver import ActionChains

from framework.support import Support

class TestBatch:
    def __init__(self, brower, support):
        self.driver = Support.get_webdriver(brower)
        self.support = support

    def main_test(self):
        self.prepare()
        self.query()
        self.batch_upload()
        self.test_2()
        self.test_3()

    def prepare(self):
        self.driver.find_element_by_link_text('批次管理').click()
        time.sleep(2)

    def query(self):
        self.driver.find_element_by_xpath("//input[@value='确认查询']").click()
        time.sleep(2)
        data = self.driver.find_element_by_xpath("//tbody[@id='batchinfo']/tr[3]/td[5]").text
        print(data)

    def batch_upload(self):
        self.driver.find_element_by_link_text("批次管理").click()
        time.sleep(2)
        self.driver.find_element_by_id('batchfile').send_keys("D:\\Other\\销售出库单-20171020-Test.xls")
        self.driver.find_element_by_xpath("//form[@class='form-inline']/div/input").click()
        time.sleep(2)

    def test_2(self):
        pass

    def test_3(self):
        pass