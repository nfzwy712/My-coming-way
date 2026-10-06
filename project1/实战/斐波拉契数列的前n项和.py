from sympy.polys.distributedmodules import sdm_deg


def funs(n):
    if n==0 or n<0:
        print('输入错误！')
        return None
    elif n==1:
        return 1
    elif n==2:
        return 2
    else:
        a,b=1,1          #第1，2项
        total= a+b       #前n项和
        for i in range(3,n+1):
            c=a+b    #a,b后一项
            total+=c
            a,b=b,c
        return total

num=int(input())
result=funs(num)
print(f"前n项和为{result}")

