import sympy as sy
import numpy as np
import matplotlib.pyplot as plt

def diff_gleichung(x, t, r):
    return sy.diff(x(t), t, 2) + sy.diff(x(t), t, 1)**2/r

# 定义参数
r = 1
t = sy.Symbol('t')
x = sy.Function('x')

# 求解微分方程
l = sy.dsolve(diff_gleichung(x, t, r), x(t))
sy.pprint(l)

# 设定初始条件（根据需要调整）
C1, C2 = sy.symbols('C1 C2')
solution = l.rhs.subs([(C1, -2), (C2, 0)])  # 替换积分常数
solution=sy.diff(solution, t,2)

# 创建数值计算函数
l_num = sy.lambdify(t, solution, modules=['numpy'])

# 计算和绘图
t_vals = np.linspace(0, 10, 1000)
l_vals = l_num(t_vals)

plt.plot(t_vals, l_vals, label='l(t)')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.ylim(-1, 1)  # 限制 y 轴范围
plt.title('Sympy')
plt.grid(True)
plt.legend()
plt.show()