f = open("F:\develop\py_project\py_grammar\单词计数文本.txt","r",encoding="UTF-8")
#方式一：读取全部内容
text = f.read()
words = text.split()  #当我此处指定为“ ”时，split只会按照空格来分因此忽略了换行符，当使用默认参数时，将所有的空白字符作为分割对象
length=len(words)
print(F'该文件中有单词{length}个')
f.close()

# 获取每一行的单词：
f = open("F:\develop\py_project\py_grammar\单词计数文本.txt","r",encoding="UTF-8")
for line in f:
    word=line.split()
    print(f"这一行的单词有这些{word}")
f.close()

