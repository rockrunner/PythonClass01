import unittest, time
from HTMLTestRunner import HTMLTestRunner
from codetest.unit_test_01 import SupportTest
from codetest.unit_test_02 import SupportTest2

# 根据测试用例和类名指定测试码顺序和指定执行哪些测试用例。
# suite = unittest.TestSuite()
# suite.addTests((SupportTest('test_check_number_02'), SupportTest('test_check_number_01'),
#                 SupportTest('test_db_query_all_01')))
# suite.addTest(SupportTest2('test_check_number_03'))
# result = unittest.TestResult()
# suite.run(result=result)
# print(result, '\n', result.failures)
# for failure in result.failures:
#     print("此处出版错误：%s" % failure[0])


# 根据测试类，直接执行其中的所有以test开头的测试用例
# suite = unittest.TestSuite()
# suite.addTest(unittest.TestLoader().loadTestsFromTestCase(SupportTest))
# suite.addTest(unittest.TestLoader().loadTestsFromTestCase(SupportTest2))
# result = unittest.TestResult()
# suite.run(result=result)
# print(result)


suite = unittest.TestSuite()
testCases01 = unittest.TestLoader().loadTestsFromTestCase(SupportTest)
testCases02 = unittest.TestLoader().loadTestsFromTestCase(SupportTest2)
suite.addTests(tests=testCases01)
suite.addTests(tests=testCases02)
# 获取当前时间
now = time.strftime("%Y%m%d_%H%M%S_")
filename = 'D:\ '+ now +'report.html'
fp = open(filename,'wb')
# 配置运行参数
runner = HTMLTestRunner(stream=fp, title=u'测试报告', description=u'执行情况汇总报告')
runner.run(suite)
fp.close()
