#产生一个随机数
import random
num=random.randint(1,20)
#输入猜测的数字
a=int(input())
if a==num:
    print("恭喜你猜对了")
else:
    if a<num:
        print("小了")
    else:
        print("大了")
    #第二次机会
    a = int(input())
    if a==num:
        print("恭喜你")
    else:
        if a<num:
            print("小了")
        else:
            print("大了")
    #第三次机会
    a = int(input())
    if a==num:
        print("恭喜你")
    else:
        print("太可惜了啊，三次都没猜对，小辣鸡")
        print(f"答案是{num}")
