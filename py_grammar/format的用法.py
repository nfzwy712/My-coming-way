#左对齐   :<宽度
a='HI'
print("{:<10}".format(a))
print("-"*30)

#右对齐    :>宽度
print("{:>10}".format(a))
print("-"*30)

#居中对齐   :^宽度
print("{:^10}".format(a))
print("-"*30)

# 自定义填充+对齐+宽度   : 填充字符 对齐方式 宽度
print("{:*<10}".format(a))
print("-"*30)

#数字格式化
num=123.456

#保留n位小数   注意此时是四舍五入的
print("{:.2f}".format(num))
print("-"*30)

