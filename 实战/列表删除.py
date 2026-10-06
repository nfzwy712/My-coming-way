# 将一个字符串转换成列表，用户输入两个数字，删除列表中这两个数字之间的元素，输出新的列表。
# 在同一行输入两个整数

s=list(input())
m,n=map(int,input().split())
#这种会直接删除，不能返回删除的元素。
del s[m:n]
print(f"这是第二次删除{s}")


#   下面是错误写法，尽量避免在遍历中使用pop以及remove，因为他们会改变索引，从而在遍历时使用会导致索引错位
result=[]
for i in range(m,n):
    r_s=s.pop(i)
    result.append(r_s)
print(f"这是第一次删除{s}")
print(result)