# 1.描述
# dict() 函数用于创建一个字典。
#
# 2.语法
# dict 语法：
#
# class dict(**kwarg)
# class dict(mapping, **kwarg)
# class dict(iterable, **kwarg)
# 3.参数说明：
#
# **kwargs -- 关键字。
# mapping -- 元素的容器，映射类型（Mapping Types）是一种关联式的容器类型，它存储了对象与对象之间的映射关系。
# iterable -- 可迭代对象。
# 4.返回值
# 返回一个字典。
# 实例
dict_1 = dict(a='a', b='b', t='t')  # 传入关键字创建字典
dict_2 = dict(zip(['one', 'two', 'three'], [1, 2, 3]))   # 映射函数方式来构造字典
dict_3 = dict([('one', 1), ('two', 2), ('three', 3)])    # 可迭代对象方式来构造字典

print(dict_1,dict_2,dict_3)