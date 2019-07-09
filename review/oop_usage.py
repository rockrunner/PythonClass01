# 类：一类事物的统称，包含：类属性，类行为。

class User:

    # User类的属性：使用类名直接调用，也可使用实例名调用，但是不建议
    user_info = [{'username':'woniu', 'password':'123456', 'balance':3000, 'phone':'13812345678'}]
    default_username = 'shanghai'

    # 构造方法: 实例化类的时候会默认调用的方法
    def __init__(self, value):
        self.username_max_count = 3
        self.password_max_count = 3
        self.phone_max_count = 3
        print("构造方法__init__正在被调用，传递的参数为：%s" % value)

    def test1(self):
        print("Test1")

    def test2(self):
        # self.test1()
        print("Test2")

    @staticmethod  # 使用装饰器（注解）staticmethod来修饰该方法，该方法则被定义为静态方法，静态方法不需要self形参，通常直接使用类名调用
    def test3():
        print("这是静态方法Test3")

    # 析构方法：类的实例不再被使用时，析构方法将会被Python解释器自动调用
    def __del__(self):
        print("当类的实例被回收时，运行该代码")


if __name__ == '__main__':
    # print(User.user_info)       # User类的属性：使用类名直接调用，也可使用实例名调用，但是不建议
    # print(User().user_info)     # 实例通常建议用于调用实例变量，而不要调用类变量
    # # print(User.username_max_count)  # 实例变量不能用类名来调用
    # print(User().username_max_count)  # 实例变量只能用实例名来调用

    # print(id(User))         # 输出User类本身的地址
    # print(id(User('')))       # 实例化User类，此称之为匿名实例，不可重用
    # print(id(User('')))       # 输出实例的地址


    # User().username_max_count += 5
    # User().username_max_count += 10
    # m1 = User().username_max_count
    # m2 = User().username_max_count
    # print(f'm1的值：{m1}，m2的值为{m2}')
    #
    # print(id(m1))
    # print(id(m2))


    user1 = User('Hello')
    user2 = User('Good')
    user3 = User('')
    user4 = User('Good')

    print(id(User))
    print(id(user1))
    print(id(user2))
    print(id(user3))
    print(id(user4))


    user1.default_username = 'nanjing'
    print(User.default_username)
    User.default_username = 'beijing'
    print(user1.default_username)
    print(user2.default_username)


    user1.username_max_count = 1000
    print(user1.username_max_count)
    print(user2.username_max_count)
    user2.username_max_count = 2000
    print(user1.username_max_count)
    print(user2.username_max_count)


    # user1.test1()
    User.test1('')