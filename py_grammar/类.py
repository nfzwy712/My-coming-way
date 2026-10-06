# 设计一个类
class Student:
    # 类的属性（成员变量）
    name=None   #将初始值设为空
    gender=None
    age=None

    # 类的行为（成员方法）
    # self是必须填写的，表示类对象本身。当我们使用类对象调用方法的时候，self会自动传入
    # 在方法内部，想访问类的成员变量时，必须使用self
    def say_hi(self):
        print(f'hi,大家好，我是{self.name}')


#创建一个可用的类对象
a=Student()   #此时的变量a即是一个对象

print("这是a的地址",a)  #这时输出的是对象a的地址，但是可以通过__str__,来实现直接输出内容

# 对象属性进行赋值
a.name='小明'
a.gender='男'
a.age=19
print(a.age)
a.say_hi()      # 注意到实际调用方法时，虽然方法的传参列表中有self参数，但是并不需要对self进行传参。但是如果传参列表中的其他参数就必须传参
print("="*50)

# 我们会发现当对象属性过多时，赋值是及其繁琐的。所以我们可以使用构造方法:  __init__（有两个特性）
#特性一：在创建类对象时，会自动执行。   特性二：在创建类对象时，将传入参数自动传递到 __init__。
class Student2:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print(f"我叫{self.name},大家好！")
    # 使用 __str__ 可以控制 类 转换 字符串 的行为
    def __str__(self):
        return f'Student2类对象，name={self.name},{self.age}岁,性别：{self.gender}'


b=Student2('小红','18',"男")
print(b)


