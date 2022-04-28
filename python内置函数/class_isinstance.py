# 1.描述
# isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。
#
# isinstance() 与 type() 区别：
#
# type() 不会认为子类是一种父类类型，不考虑继承关系。
#
# isinstance() 会认为子类是一种父类类型，考虑继承关系。
#
# 如果要判断两个类型是否相同推荐使用 isinstance()。
#
# 2.语法
# 以下是 isinstance() 方法的语法:
#
# isinstance(object, classinfo)
# 3.参数
# object -- 实例对象。
# classinfo -- 可以是直接或间接类名、基本类型或者由它们组成的元组。
# 4.返回值
# 如果对象的类型与参数二的类型（classinfo）相同则返回 True，否则返回 False。。
print(isinstance([1,3,5],list))

a = 2
print(isinstance(a,int))
print(isinstance(a,str))
print(isinstance(a,(str,int,list)))    # 是元组中的一个返回 True

#type() 与 isinstance()区别：
class A:
    pass

class B(A):
    pass


isinstance(A(), A)  # returns True
type(A()) == A  # returns True
isinstance(B(), A)  # returns True
type(B()) == A  # returns False