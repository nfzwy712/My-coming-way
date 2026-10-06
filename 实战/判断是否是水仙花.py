# 输入一个n位数，求各个数位数字的n次方之和，并判断该和是否与该数相等
a=input("请输入有一个数字：")
n=len(a)
num=int(a)
total=0
for i in range (1,n+1):
    flat=num//(10**(i-1))%10
    total+=flat**n
if total==num:
    print(f"{total},符合题目要求")
else:
    print("不符合要求")