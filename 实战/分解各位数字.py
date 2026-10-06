def func(n):
    result=tuple(n)  # tuple()、list()、set()这三个是类型构造器，在括号中加入可迭代对象，会遍历可迭代对象然后一一转换成目标类型
    print(result)
num=input()
func(num)


