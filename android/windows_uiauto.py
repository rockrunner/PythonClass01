import uiautomation, time, subprocess, os
from pykeyboard import PyKeyboard

class PyUIAuto():

    def calc_test(self):
        # 或者直接使用Python运行一个计算器
        # 启动之前先运行一条命令强制关闭所有计算器
        os.system("taskkill /f /IM Calculator.exe")

        # os.system("start /b calc.exe")
        subprocess.Popen("calc.exe")

        # 首先找到应用程序的顶层窗口
        calc_window = uiautomation.WindowControl(searchDepth=1, Name="计算器", ClassName="ApplicationFrameWindow")

        # 运行之前，如果程序已经启动，则将其放置于窗口上方
        calc_window.SetFocus()
        calc_window.SetTopmost(isTopmost=True)

        # 找到对应的该应用程序的对象进行操作
        button_3 = calc_window.ButtonControl(AutomationId="num3Button")
        button_3.Click()
        calc_window.ButtonControl(Name="加").Click()
        calc_window.ButtonControl(AutomationId="num5Button").Click()
        calc_window.ButtonControl(Name="等于").Click()

        # 得到实际运算结果并进行断言
        result = calc_window.TextControl(AutomationId="CalculatorResults").Name
        if result.split(" ")[1] == "8":
            print("测试成功.")
        else:
            print("测试失败.")

        os.system("taskkill /f /IM Calculator.exe")

        # 执行其他应用程序
        # os.system(r'"C:\Program Files\internet explorer\iexplore.exe" http://www.woniuxy.com')


    def notepad_test(self):
        os.system("start /b C:/Windows/notepad.exe")
        time.sleep(2)
        notepad = uiautomation.WindowControl(searchDepth=1, ClassName="Notepad")
        document = notepad.EditControl(AutomationId="15", Name="文本编辑器")
        document.SendKeys("这是一个文本编辑工具")  # 或使用SetValue
        notepad.MenuItemControl(Name="文件(F)").Click()
        # 按三次下箭头，再一次回车，打开文件保存对话框
        uiautomation.SendKey(uiautomation.Keys.VK_DOWN)
        uiautomation.SendKey(uiautomation.Keys.VK_DOWN)
        uiautomation.SendKey(uiautomation.Keys.VK_DOWN)
        uiautomation.SendKey(uiautomation.Keys.VK_ENTER)

        # 组合按键
        # uiautomation.Win32API.PressKey()
        # uiautomation.Win32API.ReleaseKey()

        uiautomation.SendKeys("D:\\uiauto_test4.txt")
        time.sleep(2)
        notepad.ButtonControl(Name="保存(S)").Click()
        time.sleep(2)
        notepad.ButtonControl(Name="关闭").Click()

        # os.system("taskkill /f /IM notepad.exe")

if __name__ == '__main__':
    PyUIAuto().notepad_test()
    # PyUIAuto().calc_test()
    # time.sleep(2)
    # uiautomation.MoveTo(500, 600)
    # pos = uiautomation.Win32API.GetCursorPos()
    # print(pos)