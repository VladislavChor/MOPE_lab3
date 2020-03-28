import numpy as np

x1_min = -30
x1_max = 20
x2_min = -20
x2_max = 40
x3_min = -30
x3_max = -15

x_average_max = (x1_max + x2_max + x3_max) / 3
x_average_min = (x1_min + x2_min + x3_min) / 3
y_max = 200 + x_average_max
y_min = 200 + x_average_min

m, n = 3, 4

def main(m, n):
    print("\nМатриця нормованих значень:")
    norm_x = np.array([
        [+1, -1, -1, -1],
        [+1, -1, +1, +1],
        [+1, +1, -1, +1],
        [+1, +1, +1, -1]
    ])
    for i in range(len(norm_x)):
        print("{}.".format(i + 1), end="")
        for j in range(len(norm_x[i])):
            print("{:4}".format(norm_x[i][j]), end="")
        print()

    print("\nМатриця Х:")
    x = np.array([
        [x1_min, x2_min, x3_min],
        [x1_min, x2_max, x3_max],
        [x1_max, x2_min, x3_max],
        [x1_max, x2_max, x3_min]
    ])

    for i in range(len(x)):
        print("{}.".format(i + 1), end="")
        for j in range(len(x[i])):
            print("{:4}".format(x[i][j]), end="")
        print()

    print("\nМатриця Y:")
    y = np.random.randint(y_min, y_max, size=(n, m))
    for i in range(len(y)):
        print("{}.".format(i + 1), end="")
        for j in range(len(y[i])):
            print("{:4}".format(y[i][j]), end="")
        print()

    print("\nСередні значення функції відгуку за рядками:")
    y_average = np.sum(y, axis=1) / len(y[0])
    y_1, y_2, y_3, y_4 = y_average
    print(f"y_1 = {y_1:.2f}\ny_2 = {y_2:.2f}\ny_3 = {y_3:.2f}\ny_4 = {y_4:.2f}")
    mx_1, mx_2, mx_3 = [i / len(x) for i in np.sum(x, axis=0)]
    my = sum(y_average) / len(y_average)

    a_1 = sum([x[i][0] * y_average[i] for i in range(len(x))]) / len(x)
    a_2 = sum([x[i][1] * y_average[i] for i in range(len(x))]) / len(x)
    a_3 = sum([x[i][2] * y_average[i] for i in range(len(x))]) / len(x)

    a_11 = sum([x[i][0] ** 2 for i in range(len(x))]) / len(x)
    a_22 = sum([x[i][1] ** 2 for i in range(len(x))]) / len(x)
    a_33 = sum([x[i][2] ** 2 for i in range(len(x))]) / len(x)
    a_12 = sum([x[i][0] * x[i][1] for i in range(len(x))]) / len(x)
    a_13 = sum([x[i][0] * x[i][2] for i in range(len(x))]) / len(x)
    a_23 = a_32 = sum([x[i][1] * x[i][2] for i in range(len(x))]) / len(x)

    det = np.linalg.det([[1, mx_1, mx_2, mx_3], [mx_1, a_11, a_12, a_13], [mx_2, a_12, a_22, a_32], [mx_3, a_13, a_23, a_33]])
    det_0 = np.linalg.det([[my, mx_1, mx_2, mx_3], [a_1, a_11, a_12, a_13], [a_2, a_12, a_22, a_32], [a_3, a_13, a_23, a_33]])
    det_1 = np.linalg.det([[1, my, mx_2, mx_3], [mx_1, a_1, a_12, a_13], [mx_2, a_2, a_22, a_32], [mx_3, a_3, a_23, a_33]])
    det_2 = np.linalg.det([[1, mx_1, my, mx_3], [mx_1, a_11, a_1, a_13], [mx_2, a_12, a_2, a_32], [mx_3, a_13, a_3, a_33]])
    det_3 = np.linalg.det([[1, mx_1, mx_2, my], [mx_1, a_11, a_12, a_1], [mx_2, a_12, a_22, a_2], [mx_3, a_13, a_23, a_3]])

    b_0 = det_0 / det
    b_1 = det_1 / det
    b_2 = det_2 / det
    b_3 = det_3 / det
    b = [b_0, b_1, b_2, b_3]

    print(f"\nНормалізоване рівняння регресії: y = {b_0:.5f} + {b_1:.5f} * x1 + {b_2:.5f} * x2 + {b_3:.5f} * x3\n")
    print("Перевірка:")
    y_1_ch = b_0 + b_1 * x[0][0] + b_2 * x[0][1] + b_3 * x[0][2]
    y_2_ch = b_0 + b_1 * x[1][0] + b_2 * x[1][1] + b_3 * x[1][2]
    y_3_ch = b_0 + b_1 * x[2][0] + b_2 * x[2][1] + b_3 * x[2][2]
    y_4_ch = b_0 + b_1 * x[3][0] + b_2 * x[3][1] + b_3 * x[3][2]
    print(f"y_1 = {b_0:.3f} + {b_1:.3f} * {x[0][0]} + {b_2:.3f} * {x[0][1]} + {b_3:.3f} * {x[0][2]} = {y_1_ch:.3f}"
          f"\ny_2 = {b_0:.3f} + {b_1:.3f} * {x[1][0]} + {b_2:.3f} * {x[1][1]} + {b_3:.3f} * {x[1][2]} = {y_2_ch:.3f}"
          f"\ny_3 = {b_0:.3f} + {b_1:.3f} * {x[2][0]} + {b_2:.3f} * {x[2][1]} + {b_3:.3f} * {x[2][2]} = {y_3_ch:.3f}"
          f"\ny_4 = {b_0:.3f} + {b_1:.3f} * {x[3][0]} + {b_2:.3f} * {x[3][1]} + {b_3:.3f} * {x[3][2]} = {y_4_ch:.3f}")

    print("\nКритерій Кохрена")
    f_1 = m - 1
    f_2 = n
    s_1 = sum([(i - y_1) ** 2 for i in y[0]]) / m
    s_2 = sum([(i - y_2) ** 2 for i in y[1]]) / m
    s_3 = sum([(i - y_3) ** 2 for i in y[2]]) / m
    s_4 = sum([(i - y_4) ** 2 for i in y[3]]) / m
    s_array = np.array([s_1, s_2, s_3, s_4])
    gP = max(s_array) / sum(s_array)

    # Розподіл Кохрена
    table = {3: 0.6841, 4: 0.6287, 5: 0.5892, 6: 0.5598, 7: 0.5365, 8: 0.5175, 9: 0.5017, 10: 0.4884,
             range(11, 17): 0.4366, range(17, 37): 0.3720, range(37, 145): 0.3093}
    gT = table.get(m)

    if (gP < gT):
        print(f"Дисперсія однорідна: Gp = {gP:.5} < Gt = {gT}")
    else:
        print(f"Дисперсія неоднорідна: Gp = {gP:.5} > Gt = {gT}")
        print(f'Збільшуємо m на 1')
        m = m + 1
        main(m + 1, n)
        return

    print("\nКритерій Стьюдента")
    s2_B = s_array.sum() / n
    s2_b_S = s2_B / (n * m)
    s_b_S = pow(s2_b_S, 1 / 2)

    b_0 = sum([norm_x[i][0] * y_average[i] for i in range(len(norm_x))]) / n
    b_1 = sum([norm_x[i][1] * y_average[i] for i in range(len(norm_x))]) / n
    b_2 = sum([norm_x[i][2] * y_average[i] for i in range(len(norm_x))]) / n
    b_3 = sum([norm_x[i][3] * y_average[i] for i in range(len(norm_x))]) / n

    t = [abs(b_0) / s_b_S, abs(b_1) / s_b_S, abs(b_2) / s_b_S, abs(b_3) / s_b_S]

    f3 = f_1 * f_2
    # Розподіл Стьюдента
    t_table = {8: 2.306, 9: 2.262, 10: 2.228, 11: 2.201, 12: 2.179, 13: 2.160, 14: 2.145, 15: 2.131, 16: 2.120,
               17: 2.110, 18: 2.101, 19: 2.093, 20: 2.086, 21: 2.08, 22: 2.074, 23: 2.069, 24: 2.064, 25: 2.06}
    d = 4

    for i in range(len(t)):
        if (t_table.get(f3) > t[i]):
            b[i] = 0
            d -= 1

    print(f"Рівняння регресії: y = {b[0]:.3f} + {b[1]:.3f} * x1 + {b[2]:.3f} * x2 + {b[3]:.3f} * x3")
    ch_0 = b[0] + b[1] * x[0][0] + b[2] * x[0][1] + b[3] * x[0][2]
    ch_1 = b[0] + b[1] * x[1][0] + b[2] * x[1][1] + b[3] * x[1][2]
    ch_2 = b[0] + b[1] * x[2][0] + b[2] * x[2][1] + b[3] * x[2][2]
    ch_3 = b[0] + b[1] * x[3][0] + b[2] * x[3][1] + b[3] * x[3][2]
    ck_list = [ch_0, ch_1, ch_2, ch_3]
    print("Значення нормалізовані: ", ck_list)

    print("\nКритерій Фішера:")
    f_4 = n - d
    s2_ad = m / f_4 * sum([(ck_list[i] - y_average[i]) ** 2 for i in range(len(y_average))])
    fP = s2_ad / s2_B
    # Розподіл Фішера
    fT = [
        [164.4, 199.5, 215.7, 224.6, 230.2, 234],
        [18.5, 19.2, 19.2, 19.3, 19.3, 19.3],
        [10.1, 9.6, 9.3, 9.1, 9, 8.9],
        [7.7, 6.9, 6.6, 6.4, 6.3, 6.2],
        [6.6, 5.8, 5.4, 5.2, 5.1, 5],
        [6, 5.1, 4.8, 4.5, 4.4, 4.3],
        [5.5, 4.7, 4.4, 4.1, 4, 3.9],
        [5.3, 4.5, 4.1, 3.8, 3.7, 3.6],
        [5.1, 4.3, 3.9, 3.6, 3.5, 3.4],
        [5, 4.1, 3.7, 3.5, 3.3, 3.2],
        [4.8, 4, 3.6, 3.4, 3.2, 3.1],
        [4.8, 3.9, 3.5, 3.3, 3.1, 3],
        [4.7, 3.8, 3.4, 3.2, 3, 2.9],
        [4.6, 3.7, 3.3, 3.1, 3, 2.9],
        [4.5, 3.7, 3.3, 3.1, 2.9, 2.8],
        [4.5, 3.6, 3.2, 3, 2.9, 2.7],
        [4.5, 3.6, 3.2, 3, 2.8, 2.7],
        [4.4, 3.6, 3.2, 2.9, 2.8, 2.7],
        [4.4, 3.5, 3.1, 2.9, 2.7, 2.6],
        [4.4, 3.5, 3.1, 2.9, 2.7, 2.6]
    ]
    if (fP > fT[f3][f_4]):
        print(f"fp = {fP} > ft = {fT[f3][f_4]}.\nМатематична модель неадекватна експериментальним даним\n")
    else:
        print(f"fP = {fP} < fT = {fT[f3][f_4]}.\nМатематична модель адекватна експериментальним даним\n")


print("\nРівняння регресії - y = b_0 + b_1 * x1 + b_1 * x2 + b_3 * x3")
main(m, n)