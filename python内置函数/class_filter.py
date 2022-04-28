# 1.描述
# filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换。
#
# 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
#
# 语法
# 以下是 filter() 方法的语法:
#
# filter(function, iterable)
# 参数
# function -- 判断函数。
# iterable -- 可迭代对象。
# 返回值
# 返回一个迭代器对象

#过滤列表中的奇数
def is_odd(n):
    return n % 2 == 1
tmplist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
newlist = list(tmplist)
print(newlist)

# 过滤出1~100中平方根是整数的数：
import math
def is_sqr(x):
    return math.sqrt(x) % 1 == 0


tmplist = filter(is_sqr, range(1, 101))
newlist = list(tmplist)
print(newlist)