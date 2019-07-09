import random

user_info = [{'username':'woniu', 'password':'123456', 'balance':3000, 'phone':'13812345678'},
            {'username': 'qiang', 'password': '234567', 'balance': 2000, 'phone': '15812345675'},
            {'username': 'admin', 'password': '345678', 'balance': 5000, 'phone': '17812345699'}]

# 限制次数
username_max_count = 3
password_max_count = 3
phone_max_count = 3


# 实现新用户的注册
def reg():
    username = input_username()
    password = input_password()
    phone = input_phone()
    balance = random.randrange(1000, 2000, 100)

    user_dict = {'username': username, 'password': password, 'balance':balance, 'phone':phone}
    user_info.append(user_dict)         # 为什么不需要使用global声明user_info为全局变量呢？
    print("恭喜你，注册成功。")
    print(user_info)


# 实现用户的登录
def login():
    username = input("请输入登录账号：")
    index = check_username(username)
    if index >= 0:
        password = input("请输入登录密码：")
        if user_info[index]['password'] == password:
            print("恭喜你，登录成功。")
        else:
            print("抱歉，密码不正确。")
    else:
        print("抱歉，你输入的账号不正确，请重新输入。")
        login()


# 输入用户名进行验证，直到用户输入一个可注册的用户名为止
def input_username():
    username = input('请输入注册账号：')
    global username_max_count       # 在函数体内部要修改全局变量，必须先用global声明一下
    if username_max_count == 0:
        print("你重试的次数过多，系统将退出。")
        exit(0)
    if check_username(username) >= 0:
        username_max_count -= 1
        return input_username()     # 利用递归调用的方式完成死循环
    else:
        return username

# 输入密码，直接到密码满足至少5位的条件为止
def input_password():
    password = input("请输入注册密码：")
    if len(password) < 5:
        return input_password()
    else:
        return password

# 输入电话号码并进行规则判断
# 规则：必须是数字，必须是11位，首位必须是1
def input_phone():
    phone = input("请输入注册电话：")
    if not check_phone(phone):
        return input_phone()
    else:
        return phone


# 检查电话号码的格式是否存在
def check_phone(phone):
    is_number = True
    for c in phone:
        if ord(c) < 48 or ord(c) > 57:
            is_number = False
            break

    if is_number == True and len(phone) == 11 and phone[0] == '1':
        return True
    else:
        return False


# 检查用户名是否存在，存在返回True，不存在返回False
# def check_username(username):
#     for user in user_info:
#         if username == user['username']:
#             return True
#     else:
#         return False

def check_username(username):
    for i in range(len(user_info)):
        if username == user_info[i]['username']:
            return i
    else:
        return -1



# 对check_username(username)进行简单的单元测试
# print(check_username('woniu'))
# print(check_username('admin'))
# print(check_username('zhangsan'))


if __name__ == '__main__':
    # reg()
    login()