#  输入一个混有大小写的字符串，将字符串中大小写互换，其他字符不变
#  string库中的 ascii_lowercase()返回全体小写字母，ascii_upper()返回大写字母
import string
a=input()
b=''
for c in a:
    if c in string.ascii_lowercase:
        b+=c.upper()
    elif c in string.ascii_uppercase:
        b+=c.lower()
    else:
        b+=c
print(b)