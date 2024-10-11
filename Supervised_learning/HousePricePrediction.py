# 导入必要的库
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
# 生成简单的模拟数据（假设房子的面积和价格之间的线性关系）
np.random.seed(52)  # 为了结果的可重复性
X = 2 * np.random.rand(100, 1)  # 100个随机面积数据（特征）
y = 4 + 3 * X + np.random.randn(100, 1)  # 对应的房价（目标值）

# 分割数据集为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建线性回归模型
model = LinearRegression()

# 训练模型（拟合数据）
model.fit(X_train, y_train)

# 在测试集上进行预测
y_pred = model.predict(X_test)

# 输出模型参数
print(f"模型的截距（b）： {model.intercept_}")
print(f"模型的权重（w）： {model.coef_}")

# 计算预测误差（均方误差MSE）
mse = mean_squared_error(y_test, y_pred)
print(f"均方误差： {mse}")

# 可视化结果
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体（SimHei）
plt.rcParams['axes.unicode_minus'] = False
plt.scatter(X_test, y_test, color='blue', label='真实值')
plt.plot(X_test, y_pred, color='red', label='预测值')
plt.xlabel('房屋面积')
plt.ylabel('房价')
plt.title('线性回归模型 - 房价预测')
plt.legend()
plt.show()
