# 1.描述
# slice() 函数实现切片对象，主要用在切片操作函数里的参数传递。
#
# 2.语法
# slice 语法：
#
# class slice(stop)
# class slice(start, stop[, step])
# 3.参数说明：
#
# start -- 起始位置
# stop -- 结束位置
# step -- 间距
# 4.返回值
# 返回一个切片对象。
#
# 实例
# 以下实例展示了 slice 的使用方法：

my_slice = slice(2,5,2)
array = []
for i in range(15):
    array.append(i)
print(array)
print(array[my_slice])