# 1.描述
# eval() 函数用来执行一个字符串表达式，并返回表达式的值。
#
# 2.语法
# 以下是 eval() 方法的语法:
#
# eval(expression[, globals[, locals]])
# 3.参数
# expression -- 表达式。
# globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
# locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。
# 4.返回值
# 返回表达式计算结果。
x = 7
print(eval('3 * x'))
print(eval('pow(2,2)'))
print(eval('2 + 2'))