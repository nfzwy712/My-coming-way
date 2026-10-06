# 用.将输入的字符串连接成一个字符串（第一个字符串之前没有.）
slist=input().split()
#join() 它的核心语义是：使用指定的分隔符，将一个可迭代对象（如列表、元组，字典）中的所有字符串元素连接成一个新的字符串。
#join() 要求可迭代对象中的所有元素必须都是字符串（str 类型）。如果混入了数字、None 或其他类型，会直接抛出 TypeError 错误。
result='.'.join(slist)
print(f"连接之前{slist}")
print(f"连接之后{result}")

