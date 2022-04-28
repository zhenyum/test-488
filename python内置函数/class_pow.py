# 1.描述
# pow() 方法返回 xy（x的y次方） 的值。
#
# 2.语法
# 以下是 math 模块 pow() 方法的语法:
#
# import math
#
# math.pow( x, y )
# 内置的 pow() 方法
#
# pow(x, y[, z])
# 函数是计算x的y次方，如果z在存在，则再对结果进行取模，其结果等效于pow(x,y) %z
#
# 注意：pow() 通过内置的方法直接调用，内置方法会把参数作为整型，而 math 模块则会把参数转换为 float。
#
# 3.参数
# x -- 数值表达式。
# y -- 数值表达式。
# z -- 数值表达式。
# 4.返回值
# 返回 xy（x的y次方） 的值。
import math
print(math.pow(2,4),math.pow(10,-2))