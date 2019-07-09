# user_list = ['woniu', 'zhangsan', 'lisi', 'shanghai', 'zhaoliu', 'qiang']

# 列表+字典 JSON数据格式
user_info = [{'username':'woniu', 'password':'123456', 'balance':3000, 'phone':'13812345678'},
            {'username': 'qiang', 'password': '234567', 'balance': 2000, 'phone': '15812345675'},
            {'username': 'admin', 'password': '345678', 'balance': 5000, 'phone': '17812345699'}]


def reg():
    username = input("请输入注册账号：")
    password = input("请输入注册密码：")
    phone = input("请输入电话号码：")

    for user_dict in user_info:
        if username == user_dict['username']:
            print("抱歉，账号已经存在.")
            break
    else:
        print("恭喜你，用户名可用。")

        new_user = {}
        new_user['username'] = username   # 对字典的key进行赋值，如果该key存在，则为修改，否则为新增
        new_user['password'] = password
        new_user['phone'] = phone
        new_user['balance'] = 1000

        user_info.append(new_user)

        print("恭喜你，注册成功。")
        print(user_info)


def login():
    username = input("请输入登录账号：")
    password = input("请输入登录密码：")

    for user_dict in user_info:
        if username == user_dict['username']:
            if password == user_dict['password']:
                print("恭喜你，登录成功。")
            else:
                print('抱歉，密码错误。')
            break
    else:
        print("抱歉，你输入的用户名不存在。")



if __name__ == '__main__':
    # reg()
    login()


'''
上述代码存在的问题
1. 登录和注册均需要确认用户是否存在，所以提取出来，变成一个独立的函数
2. 并不需要把用户名，密码等完全输入完成后，再来判断，浪费用户时间。
3. 电话号码需要检查格式，是否可以将电话号码的检查单独变成一个函数？
4. 用户名和密码必须是在对应的同一个字典中。
5. 如果用户名不能注册，或登录时用户名不存在，是否需要给多次机会？
'''

'''
递归调用
def test():
    username = input('请输入用户名：')
    if check_username(username):
        return test()     # 利用递归调用的方式完成死循环
    else:
        return False

print(test())
'''