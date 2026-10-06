# 所谓完数就是该数恰好等于除自身外的因子之和。输出最小的n个完数。
def func(n):
    factor=[]
    for i in range(1,n): #这不包括自身
        if n%i==0:
            factor.append(i)
    if  sum(factor)==n:
        return factor
    else:
        return None
num= int(input())
found=0
current=0
while found<num:
    factors=func(current)
    if factors:
        res='+'.join(map(str,factors))
        print(f'{current}={res}')
        found+=1
    current+=1



