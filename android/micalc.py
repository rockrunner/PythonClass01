from appium import webdriver    # 导入webdriver模块

from time import sleep
import os, subprocess

desired_caps = {}       # 定义webdriver的兼容性设置字典对象
desired_caps['platformName'] = 'Android'    # 指定测试Android平台
desired_caps['platformVersion'] = '4.4.2'   # 指定移动端的版本号
desired_caps['deviceName'] = 'Appium'       # 指定设备名称
# desired_caps['automationName'] = 'uiautomator2'
desired_caps['appPackage'] = 'com.miui.calculator'  # 指定要启动的包
desired_caps['appActivity'] = '.cal.CalculatorActivity' # 指定启动的主类程序
# desired_caps['udid'] = '127.0.0.1:62001'    # 指定模拟器设备编号(adb devices输出结果)

# 实例化webdriver，并指定appium服务器访问地址，一定要加上/wd/hub
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
sleep(3)

# 利用与webdriver一样的API接口实现对象操作
driver.find_element_by_id("btn_c_1").click()
driver.find_element_by_id("btn_5").click()
driver.find_element_by_id("btn_plus").click()
# driver.find_element_by_id("btn_7").click()
driver.find_element_by_name("7").click()
# driver.find_element_by_xpath("//android.widget.ImageView[@content-desc='等于']").click()
driver.find_element_by_accessibility_id("等于").click()
# driver.find_element_by_name("").get_attribute("text")
# 利用xpath查找运行结果并进行断言
result = driver.find_element_by_xpath("//android.widget.TextView[@text='12']")
# 由于运算结果无法直接定位，所以利用text=12来定位该元素，如果没有找到该元素，则断言失败
if result != None and result.get_attribute("text") == "12":
    print("测试成功.")
else:
    print("测试失败.")

driver.find_element_by_name("记一笔")
driver.find_element_by_accessibility_id("Content-Desc")