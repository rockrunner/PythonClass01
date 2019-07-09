import re

# 正则表达式：检验，查找/替换
# pattern = r'^1[35789]\d{9}$'
# string = '14812345678'
# result = re.match(pattern=pattern, string=string)
# if result is None:
#     print("未匹配")
# else:
#     print("已匹配")


pattern = 'value="(.*)" />'
string = '<input type="hidden" name="verify" value="44ec5b41" />'
result = re.findall(pattern, string)
print(result[0])

