# 1.描述
# issubclass() 方法用于判断参数 class 是否是类型参数 classinfo 的子类。
#
# 2.语法
# 以下是 issubclass() 方法的语法:
#
# issubclass(class, classinfo)
# 3.参数
# class -- 类。
# classinfo -- 类。
# 4.返回值
# 如果 class 是 classinfo 的子类返回 True，否则返回 False。
class A:
    print("邱波是傻逼")
class B(A):
    pass

print(isinstance(A,B))