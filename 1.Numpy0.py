import numpy as np
a= np.array([1, 2, 3, 4, 5])
b = [6,7,8,9,10]
print(a+1)
try:
    print(b + 1)
except:
    print("不能让列表直接做加减法乘除")
b = np.array(b)
print(b+1)
print("转化为数组后可以做加减乘除")
print(a+b)
print(a*b)
print(a/b)
