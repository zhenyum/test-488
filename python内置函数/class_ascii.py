# 1.描述
# ascii() 函数类似 repr() 函数, 返回一个表示对象的字符串, 但是对于字符串中的非 ASCII 字符则返回通过 repr() 函数使用 \x, \u 或 \U 编码的字符。 生成字符串类似 Python2 版本中 repr() 函数的返回值。
#
# 2.语法
# 以下是 ascii() 方法的语法:
#
# ascii(object)
# 3.参数
# object -- 对象。
# 4.返回值
# 返回字符串。

print(ascii('runoob'))
