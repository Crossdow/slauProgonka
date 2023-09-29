def progonka(a, b, c, d):
    n = len(d)
    c[0] /= b[0]  # Первый шаг прямого хода: P1 = c1/b1
    d[0] /= b[0]  # Первый шаг прямого хода: Q1 = -d1/b1

    for i in range(1, n):  # Продолжение прямого хода для i от 1 до n-1
        temp = b[i] - a[i] * c[i - 1]
        c[i] /= temp
        d[i] = (d[i] - a[i] * d[i - 1]) / temp

    x = [0] * n
    x[n - 1] = d[n - 1]  # Последний шаг обратного хода: xn = Qn

    for i in range(n - 2, -1, -1):  # Обратный ход для i от n-2 до 0
        x[i] = d[i] - c[i] * x[i + 1]  # xi = Pi * xi+1 + Qi

    return x


# Коэффициенты
a = [0, 5, -8, 6, 3]
b = [-11, -15, 11, -15, 6]
c = [-9, -2, -3, 0, 0]
d = [-122, -48, -14, -50, 42]

solution = progonka(a, b, c, d)
print("Решение системы уравнений:")
for i, x in enumerate(solution):
    print(f"x{i + 1} = {x}")
