# 将32位二进制码表示的ip地址转换为十进制格式表示的ip地址输出,中间使用'.'隔开
s=input()
if len(s) != 32:
    print("输入错误")
for i in s:
    if i!='0' and i !='1':
        print("error")
num1=int(s[0:8],2)   # int()会将后面的内容变成十进制整数，逗号后的2是 表示待更改的内容是2进制
num2=int(s[8:16],2)
num3=int(s[16:24],2)
num4=int(s[24:32],2)
print(f'{num1}.{num2}.{num3}.{num4}')


