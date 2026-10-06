def func(n):
    if n%400==0 or n%4==0 and n%100!=0:   #此处很关键因为and的优先级比or高
        print(f'{n}是闰年')
    else:
        print(f'{n}不是闰年')
year=int(input())
func(year)