# 将函数定义为 class 的成员，那么函数成为方法
"""
定义格式：与函数的区别在于class即方法的定义
class student:
    def add(self,x,y):
        return x+y
"""
# 在调用上不能像函数一样直接使用函数名调用
class Student:
    @staticmethod
    def add(x, y):
        return x + y

num=Student.add(3,4)    # 调用时通过类对象+点+函数名来调用
print(num)
print('-'*30)

# 查找某元素下标  列表.index,如果没有找到则报错ValueError
a=['asd',165,64,5864,4,5,8,6,8,4,6]
place=a.index(64)
print(place)
print('-'*30)

# 修改特定位置的元素值  语法：列表[下标]=值
a[0]=123
print(a)
print('-'*30)

#插入元素 语法：列表.insert(下标，元素)，在指定位置插入元素,之后的元素回退一格
a.insert(1,'这是插入的元素')
print(a)
print('-'*30)

# 元素的追加 语法：列表.append(元素)，将指定元素，追加到列表的尾部
a.append('这是追加的元素')
print(a)

# append只能追加一个元素，extend则可以将其他的数据容器的内容取出，依次追加到列表尾部，注意：传入参数仍为一个
a.extend(['这','是','追加的一批数据'])
print(f"追加一批元素后为{a}")
print('-'*30)

# 删除元素(指定下标)：
# 语法一：del 列表[下标]
# 语法二：列表.pop(下标)，pop实质上是取出指定位置的元素，并且从列表中删除，所以有返回值且为指定元素
del a[13]
print(a)
del_element=a.pop(13)
print(a)
print(f'\'{del_element}\'是删除的元素')   #斜杠是转义字符
print('-'*30)

# 删除元素(指定元素的内容) 语法：列表.remove(元素)，删除该元素在列表中的第一个匹配项
a=[1,1,2354,1,465,1]
a.remove(1)
print(a)
print('-'*30)

#清空列表 语法：列表.clear()
a.clear()
print(a)
print('-'*30)

# 统计某一个元素在列表中出现的次数  语法：列表.count(元素)
a=[1,2,5,1,3,5,1,5,2]
times=a.count(1)
print(f'1出现的次数为{times}次')
print('-'*30)

#统计列表中一共含有多少个元素  语法：len(列表)
length=len(a)
print(f'列表中一共有{length}个元素')



