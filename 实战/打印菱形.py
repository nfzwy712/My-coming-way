def print_diamond(n):
    if not isinstance(n, int) or n <= 0 or n % 2 == 0:
        print("错误：请输入一个正奇数作为菱形的高度！")
        return

    center = n // 2  # 计算中心行的索引
    for i in range(n):
        distance = abs(i - center)  # 当前行到中心行的距离
        spaces = ' ' * distance  # 计算左侧空格
        stars = '*' * (n - 2 * distance)  # 计算星号数量
        print(spaces + stars)
# 测试：打印一个高度为 7 的菱形
print_diamond(7)