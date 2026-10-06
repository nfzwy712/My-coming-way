import random
goal=random.randint(0,20)
times=1
answer=int(input())
while answer!=goal:
    times+=1
    if answer<goal:
        print("小了")
    else:
        print("大了")
    answer=int(input())
print(f"恭喜你猜对啦，共使用{times}次机会")


