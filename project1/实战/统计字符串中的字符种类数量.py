def funs(n):
    digit_count=0
    alpha_count=0
    space_count=0
    other_count=0
    for i in n:
       if i.isdigit():
           digit_count+=1
       elif i.isspace():
           space_count+=1
       elif i.isalpha():
           alpha_count+=1
       else :
           other_count+=1
    print(f"字符串中数字有{digit_count},空格有{space_count}个，字母有{alpha_count}个，其他字符{other_count}个")

n=input()
funs(n)