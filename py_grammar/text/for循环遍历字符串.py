#遍历字符串如下
name='abcdefg'
#注意 in 在if语句中的意思为是否存在于，而在for循环中的意思是，从字符串中取
for x in name:
    print(x)
print("-"*30)

#查找字符串中a出现的次数
times=0
test='abjksbduiabsijdbiuabsjkdbasjbdjk'
for x in test:
    if x=='a':
        times+=1
print(times)
print("-"*30)

#range(num),从0开始不包括num。
num=5
for i in range(num):
    print(i)
print("-" * 30)

#range(num1,num2)从num1开始到num2，左闭右开的区间
num1,num2=1,6
for i in range(num1,num2):
    print(i)
print("-"*30)

#range(num1,num2,step),其中step为步长，step默认为1
num1=1;num2=11
for i in range(num1,num2,2):
    print(i)
print("-"*30)



