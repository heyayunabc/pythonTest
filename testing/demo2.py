# __all__ = ['hello']
#
# hello = 'hello demo2'
#
#
# def f():
#     print("demo2 f()")
# class Demo2:
#     pass

"""
作用：zip()函数将多个可迭代的对象的元素打包成一个元组列表
语法：zip([iterable, ...])
参数：iterable一个或多个迭代器
注意：需利用list将元素释放出来
"""
# a = ['name', 'age', 'address']
# b = ["aaa", 18]
# print(list(zip(a, b)))
# print(zip(a, b))

# """
# 作用：map()函数对可迭代对象里的元素进行函数运算
# 写法：map(function, iterable, ...)
# 参数：function（函数）,iterable（一个或多个序列）
# """


# def add(x):
#     return x * 2
#
#
# print(list(map(add, [6, 7, 8, 9])))
# print(map(add, [6, 7, 8, 9]))
from filecmp import cmp

"""
作用：filter()函数过滤不符合条件的元素，返回由符合条件的元素组成的新列表
语法：filter(function, iterable)
参数：function判断函数,iterable可迭代对象
注意：需利用list将元素释放出来
"""

# def is_even(x):
#     return x % 2 == 0
#
#
# newlist = filter(is_even, [2, 5, 7, 8, 10, 11, 34])
# print(list(newlist))
# print(newlist)
"""
作用：reduce()函数会对参数序列中的元素进行累积
语法：reduce(function, iterable[, initializer])
参数：function函数(有两个参数),iterable可迭代对象, initializer初始参数(可选)
注意：在IDE编程中需要导入funtools模块
"""

# from functools import reduce
#
#
# def add(x, y):
#     return x + y
#
#
# print(reduce(add, [1, 2, 3, 4, 5]))

"""
作用：sorted()函数会对所有可迭代的对象进行排序操作
语法：sorted(iterable, cmp=None, key=None, reverse=False)
参数：
    iterable可迭代对象
    cmp【可无】比较的函数,有两个参数,参数的值都是从可迭代对象中取出.此函数必须遵守的规则为:大于则返回1,小于则返回-1,等于则返回0.
    key【可无】主要是用来进行比较的元素,只有一个参数,具体的函数的参数就是取自于可迭代对象中,指定可迭代对象中的一个元素来进行排序.
    reverse【默认升序】排序规则,reverse=True 降序,reverse=False 升序。
"""

a = [9, 8, 7, 6, 1]
print(sorted(a))  # 返回结果为：[1, 6, 7, 8, 9]
print(a)  # 返回结果为：[9, 8, 7, 6, 1]   原结果的结构不会改变

list = [('b', 2), ('a', 1), ('c', 3), ('d', 4)]
print(sorted(list, cmp=lambda x, y: cmp(x[1], y[1])))
