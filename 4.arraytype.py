import numpy as np

#产生一个含复数的数组
a = np.array([1+1j, 2+0j, 3+0j, 4+0j, 5+0j, 6+0j])
print(a)
print(type(a))
print(a.dtype)

#对于复数我们可以查看它的实部和虚部
print("实部")
print(a.real)
print("虚部")
print(a.imag)

#还可以设置它们的值
a.real = 5
a.imag = 6
print(a)

# 查看复共轭
print(a.conj()) #相当于a.conjugate()

print("\n\n\n----------------")
#事实上，这些属性方法可以用在浮点数或者整数数组上
print("事实上，这些属性方法可以用在浮点数或者整数数组上")
b = np.array([1,2,3,4,5,6])
print(b.real)
print(b.imag)
print("b的dtype是",b.dtype)
#但这里，虚部是只读的，并不能修改它的值
print("但这里，虚部是只读的，并不能修改它的值")
try:
    b.imag = 5
except Exception as e:
    print(e)
    print("b.imag = 5 会报错")

#构建数组的时候，数组会根据传入的内容自动判断类型
#对于浮点数，默认类型是float64
#对于整数，默认类型是int64
#对于复数，默认类型是complex128
#但我们也可以指定类型
print("但我们也可以指定类型")
c = np.array([1,2,3,4,5,6],dtype=np.float32)
print(c.dtype)
print(c.nbytes)
print(c.itemsize)

#转变dtype
print("转变dtype int32")
c = c.astype(np.int32)
print(c.dtype)
print(c.nbytes)
print(c.itemsize)

#除此之外，还可以指定有无符号，例如无符号整数
print("除此之外，还可以指定有无符号，例如无符号整数")
d = np.array([1,2,3,4,5,6],dtype=np.uint8)
print(d.dtype)
#uint8 只使用一个字节，表示 0 到 255 的整数。
# 还可以从二进制数据中读取。
# 先写入二进制数据：
e = np.array([66,111,121], 
          dtype=np.uint8)
e.tofile('test.bin')
# 然后读取二进制数据：
with open('test.bin', 'rb') as file:
    f = np.frombuffer(file.read(), dtype=np.uint8)
print(f)
print(np.fromfile('test.bin', dtype=np.uint8))
#可以将e中的数据作为ASCII码输出在控制台，ASCII 范围内（32-126）
print(e.tobytes().decode('utf-8'))
#tobytes() 方法将数组中的元素转换为字节对象,字节对象内部是机器可读的形式,字符串只是人类可读的形式。
#decode() 方法将字节对象转换为字符串,这样我们就可以在控制台中看到字符串了。
#也可以将字符串变成ASCII码
print(np.frombuffer(b'Girl', dtype=np.uint8))   #除了b表示字节对象，还有u表示Unicode字符串对象，f表示浮点数对象， d表示复数对象，i表示整数对象，s表示字符串对象，O表示Python对象，V表示原始数据对象，?表示布尔类型对象。

#任意类型的数组
f = np.array(['Hello',1,[1,2,3]],dtype=np.object_)
print(f)
print(f.dtype)
print('f的乘法运算')
print('f*2',f*2)

print("-----------------")
#asarray()
# np.asarray() 是 NumPy 中的一个重要函数，主要用于将输入数据转换为 ndarray 数组。它与 np.array() 类似，但有一些重要的区别：

# 1. 如果输入已经是一个 ndarray，且满足要求（数据类型等）， asarray 会直接返回输入数组的视图，而不会创建新的数组
# 2. 如果输入不是 ndarray 或需要进行数据类型转换，则会创建一个新的数组

# 1. 基本用法
# 从列表创建数组
list_data = [1, 2, 3, 4, 5]
arr1 = np.asarray(list_data)
print("从列表创建：", arr1)

# 2. 指定数据类型
arr2 = np.asarray(list_data, dtype=np.float32)
print("指定数据类型：", arr2)

# 3. 从元组创建
tuple_data = ((1, 2, 3), (4, 5, 6))
arr3 = np.asarray(tuple_data)
print("从元组创建：", arr3)

# 4. 演示 asarray 和 array 的区别
existing_array = np.array([1, 2, 3])
# asarray 不会创建新数组
arr4 = np.asarray(existing_array)
print("是否是同一个对象：", arr4 is existing_array)  # True
print("arr4",arr4)

# array 会创建新数组
arr5 = np.array(existing_array)
print("是否是同一个对象：", arr5 is existing_array)  # False
print("arr5",arr5)

# 5. 从其他序列类型创建
# 从range对象创建
arr6 = np.asarray(range(5))
print("从range创建：", arr6)

# 6. 处理嵌套序列
nested_list = [[1, 2], [3, 4], [5, 6]]
arr7 = np.asarray(nested_list)
print("从嵌套列表创建：", arr7)

# 7. 处理字符串
string_data = "Hello, World!"
arr8 = np.asarray(string_data)
print("从字符串创建：", arr8)
print("arr8的dtype是",arr8.dtype)

# 8. 处理字节序列
bytes_data = b'Hello, World!'
arr9 = np.asarray(bytes_data)
print("从字节序列创建：", arr9)
print("arr9的dtype是",arr9.dtype)

#arr8 的数据类型是 <U13 ，这是 NumPy 中的一个字符串数据类型
# 1<U13 的含义：
#    - < 表示小端字节序（little-endian）
#    - U 表示 Unicode 字符串
#    - 13 表示字符串的最大长度（这里是因为 "Hello, World!" 有13个字符）

# 这种类型的特点：
# 1. 可以存储任何 Unicode 字符
# 2. 每个字符占用 4 字节（32位）空间
# 3. 长度是固定的，由最长的字符串决定
# 4. 较短的字符串会被空字符填充到指定长度

# Unicode字符串类型示例
print("\n----- Unicode字符串类型示例 -----")
# 不同长度的字符串
str1 = np.asarray("Hello")
str2 = np.asarray("Hello, World!")
print("短字符串类型：", str1.dtype)  # 应该显示 <U5
print("长字符串类型：", str2.dtype)  # 应该显示 <U13

# 创建固定长度的Unicode字符串数组
fixed_str = np.array("Hello", dtype="U10")
fixed_str1 = np.array("Hello", dtype="U4")
print("固定长度字符串类型：", fixed_str.dtype)  # 显示 <U10
print("固定长度字符串类型：", fixed_str1.dtype)  # 显示 <U4
print("fixed_str1",fixed_str1)
print("fixed_str1会被截断，因为'hello'有5个字符，而设置dtype为U4")

# 字符串数组
str_array = np.array(['Hello', 'World'])
str_array1 = np.array(['Hello1', 'World'])
print("字符串数组类型：", str_array.dtype)  # 会自动选择合适的长度
print("字符串数组类型：", str_array1.dtype)  # 会自动选择合适的长度

#对于arr9.dtype的输出是|S13
#这里的 |S13 是 NumPy 中的字节字符串（byte string）数据类型：

# - | 表示平台字节序（platform byte-order）
# - S 表示字节字符串类型（与前面的 U Unicode 字符串不同）
# - 13 表示字符串长度
# 与前面的 Unicode 字符串（ <U13 ）相比：

# 1. 字节字符串每个字符只占用 1 个字节
# 2. 只能存储 ASCII 字符
# 3. 输出时会带有 b 前缀，表示这是字节字符串
# 这就是为什么当我们打印 arr9 时，输出的是带有 b 前缀的字符串。