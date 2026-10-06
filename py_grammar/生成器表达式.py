# 生成器表达式的语法结构非常固定，你可以把它看作是一个“带着小括号的 for 循环”。

# 基础写法（单层循环）
# 语法：(表达式 for 变量 in 可迭代对象)
# 例子：计算 0 到 4 的平方。
gen = (x ** 2 for x in range(5))
# 此时 gen 是一个生成器对象。只有在调用时才生成数据，本身不是数据。
print(type(gen))
# 我们可以用 next() 一个个取：
print(next(gen))  # 输出 0
print(next(gen))  # 输出 1
# 或者直接用 for 循环取完：
for num in gen:
    print(num)    # 依次输出 4, 9, 16

# 带条件过滤的写法（if 子句）
# 语法：(表达式 for 变量 in 可迭代对象 if 条件)
# 例子：找出 0 到 9 中所有的偶数，并计算它们的平方。
gen = (x ** 2 for x in range(10) if x % 2 == 0)
# 等价于：
# for x in range(10):
#     if x % 2 == 0:
#         yield x ** 2
print(list(gen))  # 输出 [0, 4, 16, 36, 64]


# . 多层嵌套循环的写法（多层 for）
# 语法：(表达式 for 变量1 in 可迭代对象1 for 变量2 in 可迭代对象2)
# 例子：生成两个列表的笛卡尔积（两两配对）。
list1 = [1, 2]
list2 = ['a', 'b']
gen = (f"{x}{y}" for x in list1 for y in list2)
print(list(gen))  # 输出 ['1a', '1b', '2a', '2b']

# .带条件的嵌套循环（混合写法）
# 语法：(表达式 for 变量1 in 可迭代对象1 for 变量2 in 可迭代对象2 if 条件)
# 例子：找出两个列表中，相加和为偶数的配对。
gen = (x + y for x in [1, 2, 3] for y in [4, 5, 6] if (x + y) % 2 == 0)
print(list(gen))  # 输出 [5, 7, 7, 9]