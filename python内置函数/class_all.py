# 1. 描述
# all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为TRUE，
# 如果是返回 True，否则返回 False。
#
# 元素除了是 0、空、None、False 外都算 True。
#
# 函数等价于：
#
# def all(iterable):
#     for element in iterable:
#         if not element:
#             return False
#     return True
# Python 2.5 以上版本可用。
#
#  2.语法
# 以下是 all() 方法的语法:
#
# all(iterable)
# 3.参数
# iterable -- 元组或列表。
# 4.返回值
# 如果iterable的所有元素不为0、''、False或者iterable为空，all(iterable)返回True，否则返回False；
#
# 注意：空元组、空列表返回值为True，这里要特别注意。
print(all(['a', 'b', 'c', 'd'])) # 列表list，元素都不为空或0

print(all(['a', 'b', '', 'd']))   # 列表list，存在一个为空的元素