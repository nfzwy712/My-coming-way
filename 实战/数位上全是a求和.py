#  输入两个数为a，n，计算a+aa+...+aaaa..(n个a)
a=int(input())
n=int(input())
flat=0
total=0
for i in range(0,n):
    flat+=a*(10**i)   #记录  aaaa
    total+=flat       # 求和
print(total)





