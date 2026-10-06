# 其中使用到一个print的输出不换行的写法

#此时输出换行
print("Hello")
print("World")
print("-"*30)
#此时不换行，利用end='',print函数默认自带end='\n'
print("Hello",end='')
print("World",end='')
print("-"*30)

#知识点2：使用\t符号，作用相当于在键盘上按下tab键，它是以八位为一个单位，即填满八位
# 比如打印good，good占了四位，加入\t后自动补齐到第八位，此时光标来到第九位，所以第九位是空的，光标的位置的待填入的
print("have a good day")
print("good morning sir")
print("-"*30)
print("have\ta\tgood\tday")
print("good\tmorning\tsir")#结合输出，我认为单位为四位更加合理

#打印九九乘法表
i=1
while i<=9:#控制行数
    j=1
    while j<=i :
        print(f"j*i={j*i}",end=' ')
        j+=1
    print("\n")
    i+=1




