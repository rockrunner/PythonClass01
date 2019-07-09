import unittest, time
from codetest.function import Function

class SupportTest(unittest.TestCase):

    # 重写父类方法setUp，用于对每一个测试用例设置初始化环境，类似于__init__
    # def setUp(self):
    #     self.func = Function()
    #     print("初始化方法setUp正在运行.")

    # 重写父类方法tearDown，用于对每一次的测试用例执行收尾工作，类似于__del__
    # def tearDown(self):
    #     self.func = None
    #     print("扫尾方法tearDown正在运行.")

    @classmethod
    def setUpClass(cls):
        cls.func = Function()
        print("每一个类运行时，调用一次初始化工作.")

    @classmethod
    def tearDownClass(cls):
        cls.func = None
        print("每一个类运行时，调用一次扫尾工作.")

    # 定义一个测试用例，必须以test开头
    def test_check_number_01(self):
        # assertTrue表示其参数为True，则测试成功，否则测试失败
        self.assertTrue(self.func.check_number('12345'))
        print('test_check_number_01')

    def test_check_number_02(self):
        func = Function()
        self.assertFalse(self.func.check_number('12T45'))
        print('test_check_number_02')

    def test_check_number_03(self):
        func = Function()
        self.assertEqual(self.func.check_number('-123.45'), True)
        print('test_check_number_03')

    def test_db_query_all_01(self):
        from framework.support import Support
        sql = "select username, password from user where userid < 3"
        support = Support()
        result = support.query_all(sql)
        self.assertEqual(result, (('admin', 'admin123'), ('lm', 'lm123')), '测试数据库query_all方法失败.')
        print('test_db_query_all_01')
        time.sleep(5)

if __name__ == '__main__':
    unittest.main()


# 上述代码的问题：
# 如果测试用例之间有先后关系怎么办？默认情况下，使用ASCII码顺序进行升序排列来决定运行顺序，或使用TestSuite来指定运行的测试方法
# 如果有多个测试类，又该如何调用？TestSuite来运行
# 测试报告能否有更好的解决方案？HTMLTestRunner