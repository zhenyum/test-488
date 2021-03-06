# 1.描述
# id() 函数返回对象的唯一标识符，标识符是一个整数。
#
# CPython 中 id() 函数用于获取对象的内存地址。
#
# 2.语法
# id 语法：
#
# id([object])
# 3.参数说明：
#
# object -- 对象。
# 4.返回值
# 返回对象的内存地址。
#
# 实例
# 以下实例展示了 id 的使用方法：
a = 'runbo'
print(id(a))