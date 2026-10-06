# 字符串为“背着倒梦楼红将能我”
# 从中得到红楼梦


a='背着倒梦楼红将能我'
b=a[::-1]     #将字符串反转
print(b[3:6])


a='今天，我来背红楼梦，你呢'
b=a.split('，')
print(b)
my_ord=b[1]
result=my_ord.replace('我来背',"")
print(result)