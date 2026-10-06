#  将文本翻译成二进制
#  编码有许多，所以我们要使用正确的编码本，以什么编码存入，就用什么编码来读取
#  当前通用的为 UTF-8
import time

# 打开文件
#语法：  open(name,mode,encoding),
# name:文件名 (可以包含文件所在的路径)
# mode：打开文件的模式：只读 r、写入 w、追加 a 等。w下写数据，会删除原有内容，a则将新内容加在已有内容之后。
# 当文件不存在时 w，a 均会创建新文件。
# encoding:编码格式(推荐为UTF-8) 需要注意的是  encoding 的顺序并不是第三位，所以不能使用位置传参，用关键字参数直接指定。

f = open("文件测试.txt",'r',encoding="UTF-8")
print(type(f))       # 此时的f称为 文件对象 是一个特殊的数据类型：类

#   文件对象.read(num)，num表示要读取的数据长度（字节），如果没有传入则读取全部内容。
#   文件对象.readlines()  按照行的方式对整个文件的内容进行读取，并返回一个列表，其中每一行内容作为一个元素
#   文件对象.readline()  一次只读取一行内容


# print(f.read())  # 若连续调用两次read，则第二次调用会从第一次调用结尾处（因为第一次调用的结尾处留下了标记）开始
# print("-"*30)
# print(f.readlines())   # 因为上面读取了全部内容，会留下标记，所以此时的readlines并没有读取到任何内容

# for循环读取文件行
for line in f:
    print(line)

# 文件关闭
# time.sleep(秒)将程序停在这一步多少秒,此时文件并不会停止运行，所以文件不会被关闭
# 文件对象.close()
f.close()
print("-"*30)

# with open(name,mode,encoding) as 文件对象：（可在操作完后自动close文件）
with open("文件测试.txt",'r',encoding="UTF-8") as f:
    for line in f:
        print(line)

