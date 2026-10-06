# 获取一个18位数的身份证号，输出用户的出生年月日，年龄，性别
import datetime
now_year=datetime.datetime.now().year    #  获取当前年份
number=input()
birth=number[6:10]
birth_mouth=number[10:12]
birth_day=number[12:14]
age=now_year-int(birth)
print(f"出生于{birth}年{birth_mouth}月{birth_day}日,今年{age}岁")
gender=int(number[16])
if gender%2==1:
    print("男")
else:
    print("女")


