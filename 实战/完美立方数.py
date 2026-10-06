# 当整数n>2时,关于 a**n=b**n+c**n没有正整数解。
# 当n=3时，存在四元组使得a**3=b**3+c**3+d**3成立
#  给出一个正整数N，需找到(1,N)内满足条件的四元组.b,c,d,按照大小顺序来排列。

N=int(input())
for a in range(1,N):
    A=a**3
    for b in range(1,a):
        B=b**3
        for c in range(b,a):
            C=c**3
            for d in range(c,a):
                D=d**3
                if A==B+C+D:
                    print(a,b,c,d,"满足上式")


