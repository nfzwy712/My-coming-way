#查询字典是否存在
dict1={'赵云':'1372378429'}
name=input()
if name in dict1:
    print({f'{name}:{dict1[name]}'})
else:
    print("数据不存在")

    