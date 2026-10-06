# 字符串 本身 无法修改 ,所以不能仅使用索引来更改特定位置的字符。
a='sjdkfklsdlkjflksl;kdfkj'
print("-"*30)

#可以使用 index 来 查找 指定字符首次出现的索引
b=a.index('s')
print(b)
print("-"*30)

#字符串的替换 语法：字符串.replace(字符串1，字符串2)，注意此时并不是修改了字符串本身，而是得到了一个新的字符串
a='happy birthday'
new_str=a.replace("birthday","everyday")
print(new_str)
print(a)
print("-"*30)

#字符串的分割，按照指定字符串已有的来分隔字符串，将字符串划分为多个字符串，同样的不是修改字符串本身，而是产生一个新的 列表 对象
# split()按照已有的指定字符来分割字符串。默认参数为空白字符
a='hello python hello birthday'
b=a.split(" ")
print(f"按照空格将切分后为{b}",f"b的类型是{type(b)}")
print("-"*30)

#字符串的规整（去除前后指定的字符串）,注意只是去除前后的字符，中间的会被保留
#strip()的用处是删除去除前后指定的字符串,默认参数为空白字符(空格，换行符。制表符，回车符)
old_str=" 12happy 21birthday  "
new_str=old_str.strip()
print(f"这是使用strip()后的{new_str}")
old_str="12sdlkj21"
new_str=old_str.strip("12")#注意此时12和21都会被去除，因为在传入参数是并不是将12作为一整个字符串，而是当作一个个的字符
print(f"这是使用strip(12)后的{new_str}")
print("-"*30)

# 统计字符串中字符出现的次数 语法：count
a='happy everyday'
times=a.count("a")
print(times)
print("-"*30)

#统计字符串的长度 语法：len
a="123"
long=len(a)
print(long)
print("-"*30)

#  对字符串进行大小写转换
#  upper() 将字符串中的小写字母转换为大写字母，
#  lower() 将字符串中的大写字母转换为小写字母
#  title() 将字符串中的每个单词的首字母大写，其余字母小写
#  capitalize() 将字符串的首字母大写，其余字母小写
a="hello python"
print(a.upper())
print(a.lower())
print(a.title())
print(a.capitalize())
print("-"*30)



