#  序列：可使用 下标索引 的数据容器（列表，元组，字符串）
#  切片： 语法： 序列[起始下标：结束下标：步长],  注意为 左闭右开 区间
#  注意：切片操作并不会更改原序列，而是获得一个新的子序列
my_str="ajkshdjkl16546"
my_son_str=my_str[0:4]
print(my_son_str)
print("-"*30)
my_son_str=my_str[::-1]    #将序列反转
print(my_son_str)
