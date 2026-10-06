# 百钱买百鸡问题
# 公鸡5元/只，母鸡3元/只，小鸡1元/3只，100元买100只鸡

solutions = []

# 遍历公鸡的数量 x
# 因为公鸡5元一只，100元最多买20只，所以范围是 0 到 20
for x in range(21):
    # 根据方程解得 y = (100 - 7x) / 4 计算母鸡数量
    numerator = 100 - 7 * x

    # 母鸡数量必须是正整数，所以分子必须能被4整除且结果非负
    if numerator >= 0 and numerator % 4 == 0:
        y = numerator // 4
        z = 100 - x - y  # 计算小鸡数量

        # 验证：小鸡数量必须非负，且能被3整除（因为3只1元）
        if z >= 0 and z % 3 == 0:
            solutions.append((x, y, z))

# 按照公鸡数量从小到大排列（因为x是从小到大遍历的，列表本身已有序）
solutions.sort(key=lambda item: item[0])

# 输出结果
print("公鸡\t母鸡\t小鸡")
for x, y, z in solutions:
    print(f"{x}\t{y}\t{z}")