# 1.描述
# next() 返回迭代器的下一个项目。
#
# next() 函数要和生成迭代器的 iter() 函数一起使用。
#
# 2.语法
# next 语法：
#
# next(iterable[, default])
# 3.参数说明：
#
# iterable -- 可迭代对象
# default -- 可选，用于设置在没有下一个元素时返回该默认值，如果不设置，又没有下一个元素则会触发 StopIteration 异常。
# 4.返回值
# 返回下一个项目。

# !/usr/bin/python
# -*- coding: UTF-8 -*-

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
