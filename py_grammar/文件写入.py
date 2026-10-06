import time

f=open('文件测试.txt','w')
f.write("hello world")
#  注意此时并没有将内容写入硬盘，write 只是将内容写在程序的内存中，若要将内容写入内存则还需要使用 f.flush()来刷新，将内容保存进硬盘。
f.close()
# 打开一个不存在的文件，会自动创建一个新文件
f=open('F:/text.txt','w')
f.write("hello world!!!")
f.flush()
#  不一定只能用flush来将内容写入硬盘，因为close()内置了flush的功能。

#  文件的追加，和write的区别只有模式不同，写入的函数相同。即将 w 改为 a.
#   还有即使，w写入时会清空原来的内容。



