from appium import webdriver
import time, os, random
from appium.webdriver.common.touch_action import TouchAction


class OneStroke:
    def __init__(self):
        # 配置Appium的兼容性参数Capabilities
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'   # 告诉Appium Server测试的是Android设备
        self.desired_caps['platformVersion'] = '4.4.2'  # 指定移动端的版本号
        self.desired_caps['deviceName'] = 'Appium'      # 指定设备名称
        # self.desired_caps['automationName'] = 'uiautomator2'   # 针对新版本的Android，通常批6.0以上的适用
        self.desired_caps['appPackage'] = 'com.mobivans.onestrokecharge'  # 指定要启动的包
        self.desired_caps['appActivity'] = 'com.stub.stub01.Stub01'  # 指定启动的主类程序
        self.desired_caps['udid'] = '127.0.0.1:62001'    # 指定模拟器设备编号(adb devices输出结果)

        self.desired_caps['unicodeKeyboard'] = 'True'    # 指定可输入中文
        self.desired_caps['noReset'] = 'True'           # 是否重置应用程序

        # self.desired_caps['app'] = r'D:\Workspace\pythonworkspace\HelloPython\appiumdemo\yibijizhang.apk'  # 如已安装可不指定
        # self.desired_caps['fullReset'] = 'True'          # 全部重置，包括卸载应用程序

        self.driver = webdriver.Remote('http://127.0.0.1:5000/wd/hub', self.desired_caps)

    def add_pay(self):
        time.sleep(5)
        self.driver.find_element_by_name('记一笔').click()
        self.driver.find_element_by_id("add_txt_Pay").click()
        list_type = self.driver.find_elements_by_id("item_cate_text")
        random_index = random.randrange(0, len(list_type)-1)
        list_type[random_index].click()

        self.driver.find_element_by_id('keyb_btn_9').click()
        self.driver.find_element_by_id('keyb_btn_5').click()
        remark = '类别: ' + list_type[random_index].text
        self.driver.find_element_by_id('add_et_remark').send_keys(remark)
        self.driver.find_element_by_id('keyb_btn_finish').click()
        time.sleep(3)

        try:
            self.driver.find_element_by_id('guide_img_close').click()
        except:
            pass

        list_detail = self.driver.find_elements_by_id('account_item_detail')
        first_text = list_detail[0].find_element_by_id('account_item_txt_remark').text
        first_pay = list_detail[0].find_element_by_id('account_item_txt_money').text
        if remark == first_text and first_pay == '-95':
            print("测试成功.")
        else:
            print("测试失败.")

        # 在屏幕的指定位置点击
        # TouchAction(self.driver).tap(x=400, y=500)
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        print(width, height)
        TouchAction(self.driver).tap(x=width/2, y=height/2).perform()

        time.sleep(3)

    def delete_pay(self):
        pay_detail = self.driver.find_elements_by_id('account_item_detail')[0]
        TouchAction(self.driver).long_press(pay_detail, duration=2000).perform()
        time.sleep(2)
        self.driver.find_element_by_id('alert_tv_ok').click()

        if self.driver.find_element_by_id('account_item_detail') != None:
            print("删除失败.")
        else:
            print("删除成功.")

    def start_app(self):
        self.driver.press_keycode(3)
        self.driver.find_element_by_name('浏览器').click()


if __name__ == '__main__':
    stroke = OneStroke()
    stroke.add_pay()
    stroke.delete_pay()