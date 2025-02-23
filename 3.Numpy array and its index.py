import numpy as np

#从列表转换为为数组
a= [1, 2, 3, 4, 5]
b = np.array(a)
print(a)
print(type(a))
print(b)
print(type(b))
print("----------------")
c = np.array([6,7,8,9,10])
print(c)
# 数组的类型
print("数组的类型")
print(type(c))
# 数组的元素个数
print("数组的元素个数")
print(c.size)
# 数组的元素类型
print("数组的元素类型")
print(c.dtype)
# 数组的维度
print("数组的维度")
print(c.ndim)
# 数组的形状
print("数组的形状")
print(c.shape)
# 数组所占的字节数
print("数组每个元素所占的字节数")
print(c.itemsize)
# 数组的总字节数
print("数组的总字节数")
print(c.nbytes)
'''
- c.itemsize ：表示数组中每个元素所占用的字节数
- 例如，对于一个 int32 类型的数组，每个元素占 4 个字节
- 对于 float64 类型的数组，每个元素占 8 个字节


- c.nbytes ：表示整个数组所占用的总字节数
- 计算公式： nbytes = size * itemsize
- 也就是说，总字节数等于数组中元素的个数乘以每个元素占用的字节数
'''

print("----------------")
#fill函数
d = np.array([1,2,3,4,5])
d.fill(0)
print(d)
#若fill的dtype与原数组的dtype不同，会自动进行类型转换
print(d.dtype)
d.fill(1.1)
print(d)
#d转换为float64
d = d.astype(np.float64)
print(d.dtype)
d.fill(1.1)
print(d)

#索引
e = np.array([1,2,3,4,5])
#都表示2，3
print("e[1:3]=",e[1:3])
print("e[1:-2]=",e[1:-2])
print("e[-4:-2]=",e[-4:-2])
print("e[-4:3]=",e[-4:3])
print("左闭右开")
#省略参数
print("e[1:]=",e[1:])
print("e[:3]=",e[:3])
print("以上默认步长为1")
#步长
print("步长设置")
print("e[1:4:2]=",e[1:4:2]) #步长为2
print("e[::2]=",e[::2]) #步长为2

#计算增量
print("计算增量")
lenth = np.array([1,5,71,12,15])
print("lenth[1:]-lenth[:-1]=",lenth[1:]-lenth[:-1])

#- lenth[1:] 表示从第二个元素到最后：
# - [5, 71, 12, 15]
# - lenth[:-1] 表示从第一个元素到倒数第二个元素：
# - [1, 5, 71, 12]
# - 当这两个数组相减时，会得到相邻元素之间的差值：
# - [5-1, 71-5, 12-71, 15-12]
# - 结果为： [4, 66, -59, 3]

#多维数组
f = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f)
print("f.shape",f.shape)
print("f.ndim",f.ndim)  #维度
print("f.size",f.size)
print("f.dtype",f.dtype)
#索引
print("索引")
print("f[0,0]",f[0,0])
print("f[0,1]",f[0,1])
print("f[1]",f[1])

#切片 6x6 [lower:upper:step]
g = np.arange(36).reshape(6,6)+1
print(g)
print("g[1:5,1:5]\n",g[1:5,1:5])
print("g[1:5,1:5:2]\n",g[1:5,1:5:2])

#切片是引用
print("切片是引用")
g[1:5,1:5] = 0
print(g)
print("这种现象在列表中并不会出现")
print('a',a)
print('type(a)',type(a))
a1 = a[1:3]
print('a1 = a[1:3]')
print('a1',a1)
a1[0] = 0
print("a1[0] = 0")
print('a1',a1)
print('a',a)
print("这样做的好处在于，对于很大的数组，不用大量复制多余的值，节约了空间。\
\
缺点在于，可能出现改变一个值改变另一个值的情况。\
\
一个解决方法是使用copy()方法产生一个复制，这个复制会申请新的内存：")
print("a2 = a[1:3].copy()")
a2 = a[1:3].copy()
print('a2',a2)
a2[0] = 1
print('a2[0] = 1')
print('a2',a2)
print('a',a)

#花式索引
print("花式索引")
h = np.arange(49).reshape(7,7)*10
print(h)
print("h[[0,1,2],[0,1,2]]")
print(h[[0,1,2],[0,1,2]])
print("会显示出[0,0],[1,1],[2,2]的元素，因为[0,1,2]是行的索引，[0,1,2]是列的索引")
print("还可以使用布尔数组来花式索引")
print("h[[True,False,True,False,True,False,True]]")
print(h[[True,False,True,False,True,False,True]])
print("会显示出[0,2,4,6]的元素，因为[True,False,True,False,True,False,True]是行的索引，列全部显示")
print("i = np.array([1,0,1,0,1,0,1])")
i = np.array([1,0,1,0,1,0,1],dtype=bool)
print("j = np.arange(7)")
j = np.arange(7)
print("j[i]")
print(j[i])

k = np.arange(64)+1
k.shape = (4,4,4)
#相当于k = k.reshape(4,4,4)/k= np.arage(64).reshape(4,4,4)
print(k)
y = k[:,:,[2, -1]]
print("y = a[:,:,[2, -1]]")
print(y)    # 4x4x2,[:,:,[2,-1]]表示取所有行和列，第三维的索引为2和-1,即取第三维的第2个和倒数第1个元素\

#where语句
print("where语句")
#where 函数会返回所有非零元素的索引。
# 例如，对于一个二维数组，where 函数会返回所有非零元素的行和列索引。
l = np.array([[0,1,2],[3,4,5],[6,7,8]])
print(l)
print("np.where(l)")
print(np.where(l))
print("np.where(l>3)")
print(np.where(l>3))
print("np.where(l>3)[0]")
print(np.where(l>3)[0])
print("l>3")
print(l>3)

#np.where(l>3) 返回的是一个包含两个数组的元组：
# (array([1, 1, 2, 2, 2], dtype=int64), array([1, 2, 0, 1, 2], dtype=int64))
# 这个结果的含义是：
# - 第一个数组 [1, 1, 2, 2, 2] 表示行索引
# - 第二个数组 [1, 2, 0, 1, 2] 表示列索引
# - 这两个数组是一一对应的，表示大于3的元素的位置
# 让我们把它们对应起来：
# - (1,1) -> l[1][1] = 4
# - (1,2) -> l[1][2] = 5
# - (2,0) -> l[2][0] = 6
# - (2,1) -> l[2][1] = 7
# - (2,2) -> l[2][2] = 8

# 获取索引位置
row_indices, col_indices = np.where(l>3)

# 打印每个位置的值
for row, col in zip(row_indices, col_indices):
    print(f"位置 ({row},{col}) 的值是: {l[row,col]}")