# 计算阶乘
n=int(input())
total=1
for i in range(1,n+1):
    total*=i
print(total)

# num的n次方

a=int(input())
m=int(input())
for i in range(1,m+1):
    print(a**i,end=' ')
