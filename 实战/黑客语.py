# 将一个密码转化成密语

before='12345678'
after='zbcdefgh'
#str.maketrans(before, after)
#作用：创建一个字符映射转换表（本质上是一个字典）。
#原理：它接收两个长度相同的字符串作为参数，将第一个字符串 before 中的字符与第二个字符串 after 中对应位置的字符一一映射起来。
table=str.maketrans(before,after)
a=input()
# a.translate(table)
# 作用：根据传入的映射转换表，对字符串 a 进行批量替换。
# 原理：它会遍历字符串 a 中的每一个字符，去 table（转换表）中查找。如果找到了对应的映射，就替换为转换表中的目标字符；如果没有找到，则保留原字符不变。
b=a.translate(table)
print(b)