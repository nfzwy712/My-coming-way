# 定义字典
a={"小明":16,"小红":17}

# 定义空字典
b={}          #由于字典和集合的定义均使用{}，以便区分所以定义 空集合 时使用  set()
c=dict()      #也是定义空字典，记得要加dict
print(b,type(b))
print(c,type(c))
print("-"*30)
                #同样的，key是不可以重复的
# 获取字典数据
print(a.keys())
print(a.values())
print(a["小明"])
print("-"*30)

# 字典可以嵌套
a={"小明":16,"小红":17,"嵌套":{"小刚":18,"小王":19}}
print(f'这是嵌套的展示{a["嵌套"]["小王"]}')
print("-"*30)


# 在字典中新增(更新)元素
a["小曾"]=20      # 此时的key在原字典中不存在，所以相当于新增加一个值,若此时的key存在则修改对应的value
print(f'这是新增元素的展示{a}')
print("-"*30)

#  删除元素
# 语法： 字典.pop(key),同样的可以获取被删除的value
a.pop("小曾")
print(a)
print("-"*30)

#  清空元素  字典.clear()


# 获取字典中全部的key
#  语法：字典.keys()
keys=a.keys()
print(keys)
#  遍历字典，借助上面获取到的key来遍历
for key in keys:
    print(f"字典中的key为{key}")
    print(f"字典中的value是；{a[key]}")
print("-" * 30)

#方式2：直接对字典进行for循环，每一次循环都是直接得到key
for key in a:
    print(f"key为{key}")
    print(f"value为{a[key]}")
print("-"*30)

#统计字典内的元素数量，同样使用len()
l=len(a)
print(l)