# 1.描述
# any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。
#
# 元素除了是 0、空、FALSE 外都算 TRUE。
#
# 函数等价于：
#
# def any(iterable):
#     for element in iterable:
#         if element:
#             return True
#     return False
# Python 2.5 以上版本可用。
#
# 2.语法
# 以下是 any() 方法的语法:
#
# any(iterable)
# 参数
# iterable -- 元组或列表。
# 3.返回值
# 如果都为空、0、false，则返回false，如果不都为空、0、false，则返回true。
#
# 4.实例
# 以下展示了使用 any() 方法的实例：
list_1 = [1,2,4,53,35]
tuple_1 =(0,'')
print(any(list_1),any(tuple_1))