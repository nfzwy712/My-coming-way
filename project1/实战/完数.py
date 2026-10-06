# 完数为自身等于除自身之外的因子之和
# 输出n个最小的完数
from dask.utils import factors


def funs(num):
    factors=[]
    for i in range(1,num):
        if num%i==0:
            factors.append(i)
    if sum(factors)==num:
        return factors
    else:
        return None

n=int(input())
found=0    #  已找到的个数
current=0  #  待验证数
while found<n:
    factors=funs(current)
    if factors:
        res='+'.join(map(str,factors))
        print(f"{current}={res}")
        found+=1
    current+=1


