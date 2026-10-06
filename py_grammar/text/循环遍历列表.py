# while循环遍历list
a=[1,684,465,136545,44,1,1,185,46,1654]
length=len(a)
i=0
while i<length:
    print(a[i],end=' ')
    i+=1
print('\n')


# for 循环遍历list:  可以仅使用 in 这样可以省去循环条件，仅是将list中的元素依次取出，也可以使用in range 通过索引来判断进行遍历
for i in a:
    print(i,end=' ')

