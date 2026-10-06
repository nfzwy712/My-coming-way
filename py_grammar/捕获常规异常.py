#基本语法：
# try:
#     可能发生错误的代码
# except:
#     如果出现异常，执行的代码
try:
    open("异常演示.txt",'r')
except:#(还可以加上  错误类型 （as 别名）)
    print("出现异常了,将打开模式设置为w")
    open("异常演示.txt",'w')
# except还可以指定是什么错误类型
try :
    #print(name)
except NameError:
    print("出现变量未定义的异常")