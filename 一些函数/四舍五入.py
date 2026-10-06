# 因为float()，总是会将3.455保存为3.45499999，所以这时候，我们直接使用%时总是会出现问题。但是直接输出时，会输出3.455如下：
# s='3.455'
# print(float(s))
#其实我们也可以通过+0.000001然后通过%就可以实现。


a = float(input())
# round(数值, 保留几位小数)，这里保留0位即取整
print(round(a))
# 这种写法是有bug的，并不是严格的四舍五入，0.5有时会向下取整，因为当为0.5时是取最接近的偶数。

print("-"*30)

import math
b = float(input())
#floor 是向下取整，+0.5 后向下取整等同于四舍五入
print(math.floor(b + 0.5))
print("-"*30)

# ceil是向上取整，-0.5 后向上取整等同于四舍五入
print(math.ceil(b - 0.5))
print("-"*30)

print("%.0f"%b)
print("-"*30)
# 此时能够完成四舍五入，但是输出为字符串类型而不是数。



# 最严谨的写法
from decimal import Decimal, ROUND_HALF_UP
# 保留 2 位小数，四舍五入
result = Decimal('3.14159').quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
print(result)  # 3.14

result = Decimal('3.145').quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
print(result)  # 3.15
# 常用舍入模式
# 常量	行为
# ROUND_HALF_UP	四舍五入（≥5 进位）
# ROUND_HALF_EVEN	银行家舍入（就近偶数，默认）
# ROUND_DOWN	直接截断
# ROUND_UP	远离零方向舍入
# ROUND_CEILING	向上取整
# 关键点：quantize() 用于控制小数位数，rounding 参数控制舍入策略。