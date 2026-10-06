def funs(n):
    if n%400==0:
        print("Ture")
    elif n%4==0 and n%100!=0:
        print("ture")
    else:
        print("False")
year=int(input())
funs(year)
    