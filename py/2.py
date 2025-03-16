def bisection_method(f, a, b, e):
    if f(a) * f(b) >= 0:
        print("Bisection method fails.")
        return None

    while abs(b - a) > e:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2

# 示例函数
def f(x):
    return x**3 - x - 2

# 输入参数
e = 0.0001  # 精度
a = 1       # 区间起点
b = 2       # 区间终点

# 调用二分法函数
root = bisection_method(f, a, b, e)

if root is not None:
    print(f"The root is approximately: {root}")