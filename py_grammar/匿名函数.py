#  def 定义一个有名称的函数，可以重复使用
#  lambda  定义一个无名称的函数，只能临时使用一次。
#  定义语法： lambda 传入参数：函数体 (只能写一行函数体，不能写多行)
def add(x,y):
    return x+y
print(add(1,2))

print((lambda x,y: x+y)(1,2))  #  匿名函数直接调入参数的写法

#更加规范的写法：且此时的匿名函数可以反复使用。
fun=lambda x,y: x+y
print(fun(1,2))
print(fun(2,3))

