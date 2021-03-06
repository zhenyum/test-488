# 1.描述
# int() 函数用于将一个字符串或数字转换为整型。
#
# 2.语法
# 以下是 int() 方法的语法:
#
# class int(x, base=10)
# 3.参数
# x -- 字符串或数字。
# base -- 进制数，默认十进制。
# 4.返回值
# 返回整型数据。

print(int(3.6),
int('12',16),        # 如果是带参数base的话，12要以字符串的形式进行输入，12 为 16进制
int('0xa',16),
int('10',8))
