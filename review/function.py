
user_list = ['woniu', 'zhangsan', 'lisi', 'shanghai', 'zhaoliu', 'qiang']
max_count = 5

# 检查一个用户名是否存在
# def check_user(username):
#     if username in user_list:
#         return True
#     else:
#         return False

# if check_user('lisi'):
#     print("抱歉，你注册的用户已经存在.")
# else:
#     print("恭喜你，用户名可用。")


def change_global():
    global max_count    # 将max_count声明为全局变量
    print(max_count)
    max_count = 100
    print(max_count)    # 读取全局变量的值是没有问题的

# Python中函数的参数的类型和使用
def test_args(a, b, c=300, *args, **kwargs):
    print("--------------------")
    print(f'固定位置参数：a的值为{a}，b的值为{b}')    # 位置参数的值必须传递
    print(f'默认值参数c的值为{c}')                   # 默认值参数可以传实参，也可以不传
    print(f'可变参数args的值为{args}')               # 可变参数可以传值，可以不传，有值，则按照参数的顺序取值，且存到元组中
    print(f'关键字参数kwargs的值为{kwargs}')         # 关键字参数的值可传可不传，如有值，则必须以key=value的方式指定实参

# 关于函数中参数的传值和传地址
# 对于不可变数据类型，传值，对于可变数据类型，传地址。
def test_addr(number, string, list):
    print(f"参数的值为{number}, {string}, {list}")
    number += 5000
    print('形参number变量的地址为：%d' % id(number))
    string = '蜗牛学院'
    # list = [111, 222, 333, 444, 555]
    list.append(6)
    list.append(7)
    list[0] = 111
    print('形参list变量的地址为：%d' % id(list))
    print(f"参数的值为{number}, {string}, {list}")

if __name__ == '__main__':
    # change_global()

    # test_args(100, 200)
    # test_args(b=200, a=100)
    # test_args(100, 200, 301)
    # test_args(100, 200, 301, 400, 500, 600)
    # test_args(100, 200, 301, 400, 500, 600, name='Woniu', age=30, addr='上海')
    # test_args(100, 200, name='Woniu', age=30, addr='上海')
    # test_args(100, 600)
    # test_args(600, b='Woniu', age=30, addr='上海')


    number = 2000
    print('实参number变量的地址为：%d' % id(number))
    string = '海螺学院'
    list = [1, 2, 3, 4, 5]
    print('实参list变量的地址为：%d' % id(list))
    test_addr(number, string, list)
    print(f"实参传递完成后，实参最终的值：{number}, {string}, {list}")