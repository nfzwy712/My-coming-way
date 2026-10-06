#  操作文件，对文件内容进行备份。

#打开文件获取文件对象，准备读取。
fr=open("文件测试.txt",'r')
fw=open("文件测试.txt.bat",'a')
for i in fr:
    fw.write(i)
print('备份已完成')
fw.close()
fr.close()
