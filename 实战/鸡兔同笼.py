#  输入脚的个数以及头的个数，计算一共有多少只鸡多少只兔，如果，输入的数据不符合实际则提示“输入不符合实际”

head=int(input())
fleet=int(input())
if fleet < head*2 or fleet > head*4 or fleet%2!=0:
    print("输入不符合实际")
else:
    tu=(fleet-head*2)//2
    ji=head-tu
    print(f"兔子有{tu}只，鸡有{ji}只")