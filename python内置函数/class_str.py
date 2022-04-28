# 1.描述
# str() 函数将对象转化为适于人阅读的形式。
#
# 2.语法
# 以下是 str() 方法的语法:
#
# class str(object='')
# 3.参数
# object -- 对象。
# 4.返回值
# 返回一个对象的string格式。
print(str('adgdg'))
dict_1 = {'dfdf': 'dfdf.com', 'google': 'google.com'};
dict_2 = str(dict_1)
print(type(dict_2))