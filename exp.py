import csv
import matplotlib.pyplot as plt

factor = 1
up = 1000

# 从CSV文件中读取数据，每一行分别对应x y1 y2
x = []
y1 = []
y2 = []
with open('data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    i = 0
    for row in csvreader:
        if i == 0:
            x = [int(item) for item in row[:up]]
        elif i == 1:
            y1 = [float(item) * factor for item in row[:up]]
        elif i == 2:
            y2 = [float(item) * factor for item in row[:up]]
        i += 1

# 计算两个折线图之间的差值(倍数)
diff = [(y1_val + 1e-8) / (y2_val + 1e-8) for y1_val, y2_val in zip(y1, y2)]

plt.figure(1)

plt.plot(x, y1, label='Base elapsed time')
plt.plot(x, y2, label='Optimize elapsed time')

# 添加标题和标签
plt.title(f'')
plt.xlabel('长度，个数等变量')
plt.ylabel('Elapsed Time')

# 添加图例
plt.legend()

plt.figure(2)
plt.plot(x, diff, label='Factor of improvement', linestyle='--')
# 展示所有图
plt.show()
