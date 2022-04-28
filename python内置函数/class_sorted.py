# 1.描述
# sorted() 函数对所有可迭代的对象进行排序操作。
#
# sort 与 sorted 区别：
#
# sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
#
# list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
#
# 2.语法
# sorted 语法：
#
# sorted(iterable, key=None, reverse=False)
# 3.参数说明：
#
# iterable -- 可迭代对象。
# key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
# reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。
# 4.返回值
# 返回重新排序的列表。
list = [11,34,5,21,3434,33,54,343,435,99]
tuple_1 = (11,34,5,21,3434,33,54,343,435,99)

print(sorted(list),sorted(tuple_1))