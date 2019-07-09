# 对代码级接口进行测试，实现其测试驱动程序
from codetest.function import Function

# def test_check_number():
#     function = Function()
#
#     if function.check_number('123.45') == True:
#         print("测试123.45成功.")
#     else:
#         print("测试123.45失败.")
#
#     if function.check_number('123T45') == False:
#         print("测试123T45成功.")
#     else:
#         print("测试123T45失败.")
#
#     if function.check_number('-123.45') == True:
#         print("测试-123.45成功.")
#     else:
#         print("测试-123.45失败.")


# 测试驱动程序做三件事：定义期望结果，调用被测对象，对比实际结果。


def test_check_number(number, expect):
    function = Function()
    actual = function.check_number(number)
    if actual == expect:
        print("测试 %s 成功." % number)
    else:
        print("测试 %s 失败." % number)


# 调用测试驱动程序test_check_number，完成测试用例的输入的运行
test_check_number('123.45', True)
test_check_number('-123.45', True)
test_check_number('12345', True)
test_check_number('0.12345', True)
test_check_number('123T45', False)
test_check_number('12.3.45', False)
test_check_number('-123-45', False)
test_check_number('123-45', False)
test_check_number('0.000000000001', True)
test_check_number('-', False)
test_check_number('-.', False)
test_check_number('', False)



# 请对Support类的query_all的方法。
from framework.support import Support
sql = "select username, password from user where userid < 3"
support = Support()
# result = support.query_all(sql)[0][0]
# if result == (('admin', 'admin123'), ('lm', 'lm123')):
# if result == 'admin':
result = support.query_all(sql)
if len(result) == 2:
    print("测试成功")
else:
    print('测试失败')


# 真实的代码级接口测试，甚至于白盒测试，有三个重点需要消耗大量精力：
# 1. 并不是每一个被测接口，都有返回值，如果没有返回值，那么如何断言？即使没有返回值，那么一定有该被测代码的行为结果，根据结果来断言。
# 2. 并不是每一个被测接口的参数都是基础类型，直接可以传值，有些时候为了构造一个参数，写的代码可能比被测代码都多。
# 3. 并不是每一个被测接口都是很方便进行直接调用的，有可能需要间接调用，当然这也是接口测试的价值所在。


import os, time
filename = time.strftime('%Y%m%d_%H%M%S') + '.txt'
print(os.path.abspath('..'))
file_path = os.path.abspath('..') + '/framework/result/' + filename
support.write_result(file_path, 'Hello Python.')
time.sleep(2)
if os.path.exists(file_path):
    print("测试成功.")
else:
    print("测试失败.")

