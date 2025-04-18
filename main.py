import sympy as sy
from sympy.physics.units import gravitational_constant as g
import matplotlib.pyplot as plt
def diff_gleichung(x,t,r):
    return sy.diff(x(t),t,2)+sy.diff(x(t),t,1)**2/r
'''r=input("Raius von der Kurve:")
theta=input("Steigung in Radian:")
f=input("Antriebskraft:")
m=input("Masse:")'''
r=0.7
x=sy.Function('x')
t=sy.symbols('t')
l=sy.dsolve(diff_gleichung(x, t,r),x(t))
sy.pprint(l)
# 第二步：将符号函数转为可计算的函数
f_lambdified = sp.lambdify(x, f_sym, modules=['numpy'])

# 第三步：创建数值范围并计算函数值
x_vals = np.linspace(-5, 5, 400)
y_vals = f_lambdified(x_vals)

# 第四步：绘图
plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label='f(x) = sin(x) * exp(-x²)')
plt.title("Sympy Function Plot using Matplotlib")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()