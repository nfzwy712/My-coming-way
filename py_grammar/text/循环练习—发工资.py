import random
total=10000
performance=random.randint(1,10)
for i in range(1,21):
    performance = random.randint(1, 10)
    if performance>5:
        print(f'员工{i}绩效为{performance}发工资1000元')
        total=total-1000
    else:
        print(f"员工{i}绩效为{performance}不够，不发工资")
        continue

