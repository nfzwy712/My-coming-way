#设计一个函数，参数为正整数，返回斐波拉契数列的前n项之和。
def func(n):
    # 1. 先把边界条件放在最前面处理
    if n <= 0:
        return 0
    if n == 1:
        return 1

    # 2. 初始化斐波那契数列的前两项，以及前两项的和
    f1 = 1
    f2 = 1
    total = 2  # 前两项的和 (1 + 1)

    # 3. 因为前两项已经算过了，所以只需要再循环 n-2 次
    for i in range(n - 2):              # 当输入2时。循环条件为 i in range(0),这在python中属于是空序列所以不会进入循环。
        fn = f1 + f2  # 算出下一项
        total += fn  # 把下一项加到总和里
        f1 = f2  # 更新前两项，准备计算再下一项
        f2 = fn
    return total

num= int(input())
print(func(num))