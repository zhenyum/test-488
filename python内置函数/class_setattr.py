# 1. 描述
# setattr() 函数对应函数 getattr()，
# 用于设置属性值，该属性不一定是存在的。
#
# 2. 语法
# setattr() 语法：
#
# setattr(object, name, value)
# 3. 参数
# object -- 对象。
# name -- 字符串，对象属性。
# value -- 属性值。
# 4. 返回值
# 无。

class A():
    name = "runoob"
a = A()
setattr(a, "age", 28)
print(a.age)
