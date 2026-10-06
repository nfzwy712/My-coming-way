#不支持元素重复，且无序,所以无法使用索引，但是允许修改
#集合定义使用{}

I={"邵东一中","湖南工商大学"}   # 不限数据类型
empty_set=set()   #定义空集合
print(type(I),type(empty_set))
print("-"*30)

#添加元素
# 语法：set.add(元素)
I.add("水井头中学")
print(I)
print("-"*30)

#移除某个元素
I.remove("水井头中学")
print(I)
print("-"*30)

# 随机取出一个元素，列表中可用pop从列表取出指定下标的元素，但是由于集合没有下标索引，所以随机取出一个元素,同样的是将该元素从集合(列表)中删除
result=I.pop()
print(result)
print(I)
print("-"*30)

#清空集合   集合名.clear()
I.clear()
print(I)
print("-"*30)

#  取两个集合的差集
#  语法 ：集合1.difference(集合2)，是得到一个新集合不改变旧集合
set_a = {1,2,3,4}
set_b = {4,5,6,7}
set_re=set_a.difference(set_b)
print(f"取差集为{set_re}")
print("-"*30)

# 消除两个集合的差集
# 语法：集合1.difference_update(集合2),该函数无返回值,   对集合1直接更改
set1={1,2,3,4}
set2={4,5,6,7}
set1.difference_update(set2)
print(set1)
print(set2)
print("-"*30)


# 将两个集合合并为一个
# 语法：集合1.union(集合2)
new_set=set1.union(set2)
print(f"两个集合合并为{new_set}")
print("-"*30)

# 集合的遍历
for i in set1:
    print(i,end=' ')


