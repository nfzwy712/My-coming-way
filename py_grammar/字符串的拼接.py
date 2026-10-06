# 第一种方式可以用 + 直接拼接，但是只能拼接两个字符串
name='小明'
name2='小刚'
friend=name+name2
print(friend)

# 第二种方式（字符串的格式化）：通过占位来实现拼接，此时不局限于数据类型
#  %s 的意思是我先占一个位置，我将把变量转化成字符串放到占位的位置
age=19
name='小明今年%s岁'%age
print(name)

# 拼接多个字符串用括号括起来，在括号内按照顺序排列
gender='男'
name='小明，性别%s,年龄%s'%(gender,age)
print(name)
#此时是将数字转化成字符串来拼接

#同时还存在%d，以及%f分来来对应整数和浮点数，这样在拼接时便不会将数据类型改变
name='小明的年纪是%d'%age
print(name)
print('-'*30)

a=20.211
money='零花钱%f'%a
print(money)
#此时精度未得到控制

# 可以使用 m.n 来控制精度，m(控制宽度)要求是数字（很少使用），设置的宽度小于数字本身。n 控制小数点精度，要求是数字，会进行四舍五入.
a=11
money='%5d'%a  #此时的5为上述m,此时会在11前加上三个空格，以保证为五个宽度
print(money)
money='%.2f'%a
print(money)

# 四舍五入
a=11.357
money='%.2f'%a
print(money)
# 不四舍五入
print(f"不四舍五入的结果为{a:<.2f}")

#第三种方式：通过语法：f"内容{变量}"的格式来实现快速格式化。注意字符串前加f，f是一个标志
# 特点：不限数据类型，不做精度控制只将变量原封不动放入大括号位置.
name='小明'
age=19
money=11.11
print(f"{name}今年{age}岁,有存款{money}元")
print("-"*30)

#  注：可以直接格式化表达式，即在%后或者{}中直接填入表达式。这样可以简化代码。

#还可以使用format来进行格式化，
money=12.456
print("{:.2f}".format(money))


# 使用join()，将一个可迭代对象（如列表、元组等）中的多个字符串元素，用指定的分隔符连接起来，最终生成一个新的字符串。
# 假如我想去除字符串中的空白字符
my_str=("sidjh"
        "sdofkgjg  esdioj       iajodof      pqowerjkt")
new_str="".join(my_str.split())  # 将字符串按照空白字符分割生成一个列表。
print(f"这是去除空白字符后的{new_str}")







