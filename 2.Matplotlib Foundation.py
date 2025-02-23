import matplotlib.pyplot as plt
import numpy as np
plt.ion()   # 开启交互模式
# plt.close()  # 关闭所有图形窗口
# plt.ioff()  # 关闭交互模式

# 解决负号显示问题
plt.rcParams['axes.unicode_minus'] = False  
#更改画图子体为黑体
plt.rcParams['font.sans-serif'] = ['SimHei']

plt.figure()  # 创建新的图形窗口
# 生成 x 值，范围从 0 到 2π，共 50 个点
x = np.linspace(0, 2 * np.pi, 50)
# 计算 sin(x) 的值
y = np.sin(x)
y1 = np.cos(x)
# 绘制二维图
# 在 matplotlib 里，plt.plot(y) 这样调用时，x 轴不设置是可行的。当你仅向 plt.plot() 函数传入一个数组 y 时，matplotlib 会默认把数组 y 的索引当作 x 轴的值，也就是 x 轴的值为 [0, 1, 2, ..., len(y)-1]
plt.plot(y)
# 显示图形
plt.show()
plt.figure()  # 创建新的图形窗口
plt.plot(x,y)   #与plot(y)相同
plt.plot(x,y1)
plt.show()
# 为随机散点图生成数据
size = np.random.rand(50) * 100
color = np.random.rand(50)

# 为柱状图生成数据
categories = ['A', 'B', 'C', 'D', 'E']
values = np.random.rand(5) * 100

#---------------------------------

# 创建一个大图布局，包含所有子图
plt.figure(figsize=(15, 10))  # 设置整体图形大小
#- 第一个数字 15 表示宽度（单位：英寸）
#- 第二个数字 10 表示高度（单位：英寸）

# - figsize=(15, 10) 会影响所有子图的大小
# - 因为它设置了整个画布的大小，子图会在这个画布内按比例分配空间
# - 每个子图的实际大小 = 总画布大小 ÷ 网格划分

# 创建6个子图的网格布局
plt.subplot(2, 3, 1)  # 第一个子图：简单的sin曲线
plt.plot(y)
plt.title('简单sin曲线')

plt.subplot(2, 3, 2)  # 第二个子图：sin和cos曲线
plt.plot(x, y)
plt.plot(x, y1)
plt.title('sin和cos曲线')

plt.subplot(2, 3, 3)  # 第三个子图：不同线型的sin
plt.plot(x, np.sin(x), 'r-^')
plt.plot(x, np.sin(x+1), 'b--s')
plt.plot(x, np.sin(x+2), 'g:o')
plt.plot(x, np.sin(x+3), 'm-.D')
plt.legend(['sin(x)实线', 'sin(x+1)虚线', 'sin(x+2)点线', 'sin(x+3)点划线'], fontsize='small')
plt.title('不同线型的sin')

plt.subplot(2, 3, 4)  # 第四个子图：心形散点图
t = np.linspace(0, 2 * np.pi, 100)
x_heart = 16 * np.sin(t) ** 3
y_heart = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
plt.scatter(x_heart, y_heart, color='red', marker='o')
plt.title('心形散点图')

a = np.random.rand(50)
b = np.random.rand(50)
plt.subplot(2, 3, 5)  # 第五个子图：随机散点图
plt.scatter(a, b, s=size, c=color, cmap='viridis')
plt.colorbar()
plt.title('随机散点图')

plt.subplot(2, 3, 6)  # 第六个子图：柱状图
plt.bar(categories, values)
plt.title('柱状图示例')
# 调整子图之间的间距
plt.tight_layout()
# 显示整体图形
plt.show()

#---------------------------------
#柱状图参数
plt.figure()  # 创建新的图形窗口
#设置颜色，透明度，边框，宽度，边框颜色，边框宽度等参数
plt.bar(categories, values, color='skyblue', alpha=0.7, edgecolor='black', linewidth=1.5)  # 设置颜色、透明度、边框等参数
plt.show()



# 堆叠柱状图
plt.figure()  # 创建新的图形窗口
# 生成数据
categories = ['A', 'B', 'C', 'D', 'E']
values1 = np.random.rand(5) * 100
values2 = np.random.rand(5) * 100
# 绘制堆叠柱状图
plt.bar(categories, values1, color='skyblue', label='值 1')
# bottom 参数设置为 values1，使得 values2 堆叠在 values1 上方,bottom=values1 表示将 values2 堆叠在 values1 的顶部
plt.bar(categories, values2, bottom=values1, color='lightcoral', label='值 2')
# 添加图例
plt.legend()
# 显示图形
plt.show()


#标签设置
#设置在plot函数中
# 除了以上的图类型之外还有:圆形图，饼图，直方图，散点图，箱线图，热力图，等高线图，极坐标图，3D图，折线图等
#直方图
plt.figure()  # 创建新的图形窗口
# 生成数据
data = np.random.randn(1000)
# 绘制直方图
plt.hist(data, bins=30, color='skyblue', edgecolor='black',label='直方图')
# 添加标题和标签
plt.title('直方图示例')
plt.xlabel('值')
plt.ylabel('频率')
# 添加图例
plt.legend()
# 显示图形
plt.show()



#叠加直方图
plt.figure()  # 创建新的图形窗口
# 生成数据
data1 = np.random.randn(1000)
data2 = np.random.randn(1000)
# 绘制直方图
plt.hist(data1, bins=30, color='skyblue', edgecolor='black',label='数据 1')
plt.hist(data2, bins=30, color='lightcoral', edgecolor='black',label='数据 2')
# 添加标题和标签
plt.title('叠加直方图示例')
plt.xlabel('值')
plt.ylabel('频率')
# 添加图例
plt.legend()
# 显示图形
plt.show()




# 箱线图
plt.figure()  # 创建新的图形窗口
# 写入数据
data = np.random.randn(100)
# 绘制箱线图
plt.boxplot(data, labels=['数据'], patch_artist=True, boxprops=dict(facecolor='skyblue'))
# 添加标题和标签
plt.title('箱线图示例')
plt.xlabel('数据')
plt.ylabel('值')
# 显示图形
plt.show()



'''
cla() 方法用于清除当前坐标轴上的绘图，保留当前图像坐标轴。
clf() 方法用于清除当前图像窗口中的绘图，保留当前窗口。
close() 方法用于关闭当前图像窗口，释放内存资源。
'''

#多个箱的箱线图
plt.figure()  # 创建新的图形窗口
# 写入数据
#X轴(样本1，样本2，样本3)
#Y轴(样本1的值，样本2的值，样本3的值)
data = [np.random.randn(100), np.random.randn(50) + 1, np.random.randn(10) + 2]
#- np.random.randn(100) ：生成100个服从标准正态分布（均值为0，标准差为1）的随机数
# - np.random.randn(50) + 1 ：生成50个随机数，并且整体加1（使其均值为1）
# - np.random.randn(10) + 2 ：生成10个随机数，并且整体加2（使其均值为2）

# 绘制箱线图
plt.boxplot(data, labels=['样本 1', '样本 2', '样本 3'], patch_artist=True, boxprops=dict(facecolor='skyblue'))
# 添加标题和标签
plt.title('多个箱的箱线图示例')
plt.xlabel('样本')
plt.ylabel('值')
# 显示图形
#grid()函数用于添加网格线
plt.grid()
plt.show()


# 创建第一个图
plt.figure(80)
plt.plot([1, 2, 3], [1, 2, 3], 'r-')
plt.title('第一个图')
plt.show()  #每次调用 plt.show() 后，matplotlib 会清除当前图形的内容。
plt.figure(80)
# 在同一个窗口中绘制新的图
plt.plot([1, 2, 3], [3, 2, 1], 'b--')
plt.title('第二个图')
plt.show()


plt.figure()
plt.plot([1, 2, 3], [1, 2, 3], 'r-')
plt.plot([1, 2, 3], [3, 2, 1], 'b--')
plt.title('两个图')
plt.show()


plt.figure()
plt.plot([1, 2, 3], [1, 2, 3], 'r-')
plt.title('第一个图')
plt.draw()
plt.pause(1)  # 暂停一下让图形显示出来
plt.plot([1, 2, 3], [3, 2, 1], 'b--')
plt.draw()
plt.pause(1)
plt.cla()  # 清除当前图形
plt.pause(1)
plt.plot(0,0,'ro',markersize=10)    #红色，大小为10的圆点
plt.draw()
plt.pause(1)
plt.show()  # 显示并保持窗口


'''
Matplotlib 支持的主要图表类型及其标签支持情况如下：

1. 基础图表（支持 label 参数）：
- 折线图 (plot)
- 散点图 (scatter)
- 柱状图 (bar)
- 直方图 (hist)
- 饼图 (pie)
- 面积图 (fill_between, fill)
2. 统计图表：
- 箱线图 (boxplot) - 使用 labels 参数而不是 label
- 小提琴图 (violinplot) - 使用 labels 参数
- 误差条形图 (errorbar) - 支持 label
- 核密度图 (kde) - 支持 label
3. 特殊图表：
- 等高线图 (contour/contourf) - 支持 label
- 热力图 (heatmap) - 不支持 label，但可以添加 colorbar
- 极坐标图 (polar) - 支持 label
- 雷达图 - 支持 label
- 气泡图 - 通过 scatter 实现，支持 label
4. 3D 图表（支持 label）：
- 3D 散点图 (scatter3D)
- 3D 曲面图 (surface)
- 3D 线图 (plot3D)
- 3D 柱状图 (bar3d)
5. 组合图表：
- 堆叠图（所有类型都支持 label）
- 多轴图（每个子图都支持相应的标签设置）
特别说明：

1. 有些图表虽然不直接支持 label 参数，但可以通过其他参数（如 labels）来添加标签
2. 某些图表类型的标签是通过其他方式实现的，比如：
   - colorbar 的标签
   - 坐标轴标签 (xlabel/ylabel)
   - 图例标签 (legend)
'''


plt.ioff()
plt.close("all")

plt.show()
# 图像显示演示
plt.figure()
# 创建一个简单的灰度图像数组
image_data = np.random.rand(100, 100)  # 100x100的随机灰度图
plt.imshow(image_data, 
          extent=[-25, 25, -25, 25],  # 设置坐标范围
          cmap=plt.cm.bone)           # 设置颜色映射
plt.colorbar()  # 添加颜色条
plt.title('随机灰度图 - bone配色')
plt.show()

# 使用不同的colormap显示同一图像
plt.figure(figsize=(15, 5))
# 创建1行3列的子图
plt.subplot()
plt.imshow(image_data, cmap=plt.cm.hot)
plt.colorbar()
plt.title('hot配色')

plt.subplot()
plt.imshow(image_data, cmap=plt.cm.cool)
plt.colorbar()
plt.title('cool配色')

plt.subplot()
plt.imshow(image_data, cmap=plt.cm.rainbow)
plt.colorbar()
plt.title('rainbow配色')

plt.tight_layout()  # 调整子图间距
plt.show()

# 创建一个简单的彩色图像
color_image = np.zeros((100, 100, 3))  # 100x100的RGB图像
color_image[:, :, 0] = np.linspace(0, 1, 100)  # R通道
color_image[:, :, 1] = np.linspace(0, 1, 100)[:, np.newaxis]  # G通道
color_image[:, :, 2] = np.outer(np.linspace(0, 1, 100), np.linspace(0, 1, 100))  # B通道

plt.figure()
plt.imshow(color_image)
plt.title('RGB彩色图像示例')
plt.colorbar()
plt.show()

# 显示图像数组信息
print("灰度图像形状:", image_data.shape)
print("彩色图像形状:", color_image.shape)

#查看cm的种类
print("可用的颜色映射:")
print(plt.colormaps())