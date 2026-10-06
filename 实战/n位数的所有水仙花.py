# 水仙花是指n位数，其中n>=3且n<6,她的每个数位上的数的n次幂之和等于它本身
n=int(input())
start=10**(n-1)
end=10**n
for i in range(start,end):
    digits=list(map(int,str(i)))
    total=sum(digit**n for digit in digits)  # sum()内置了遍历/索取的能力，所以才可以直接对生成器对象进行求和。
    if total==i:
        print(f'{total}是水仙花')


