import uiautomation
import time, random, os

def calc_test():
    os.system('calc.exe')
    time.sleep(2)
    calcwin = uiautomation.WindowControl(Name='计算器', searchDepth=1)
    print(calcwin.BoundingRectangle)
    # calcwin.Maximize()
    calcwin.ButtonControl(Name='三', AutomationId='num3Button').Click()
    calcwin.ButtonControl(AutomationId='plusButton').Click()
    calcwin.ButtonControl(Name='五').Click()
    calcwin.ButtonControl(Name='等于').Click()
    time.sleep(1)

    # searchDepth参数：查找窗口时，设置为1可以加快查找速度，查找控件时，可以选择不设置，否则可能因为深度不对而找不到。
    result = calcwin.TextControl(AutomationId='CalculatorResults', searchDepth=1).Name
    print(result)
    if result == '显示为 8':
        print("测试成功")
    else:
        print('测试失败')


calc_test()