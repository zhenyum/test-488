# 1.描述
# sum() 方法对序列进行求和计算。
#
# 2.语法
# 以下是 sum() 方法的语法:
#
# sum(iterable[, start])
# 3.参数
# iterable -- 可迭代对象，如：列表、元组、集合。
# start -- 指定相加的参数，如果没有设置这个值，默认为0。
# 4.返回值
# 返回计算结果。
print(sum([0,1,2]))
print(sum((2, 3, 4), 1))       # 元组计算总和后再加 1
print(sum([0,1,2,3,4], 2))      # 列表计算总和后再加 2
