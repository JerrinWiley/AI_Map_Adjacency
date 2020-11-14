import random


def RHC(sp, p, z, seed):
    random.seed(seed)
    x, y = sp[0], sp[1]
    solution_count = 1
    min_function = pow(pow(x, 2) + y - 11, 2) + pow(x + pow(y, 2) - 7, 2)
    func = min_function
    flag = False
    while func != min_function or flag == False:
        flag = True
        for i in range(p):
            z1 = random.uniform(-z, z)
            z2 = random.uniform(-z, z)
            minimize_f = pow(pow(x + z1, 2) + (y + z2) - 11, 2) + pow(((x + z1) + pow((y + z2), 2) - 7), 2)
            if min_function > minimize_f:
                min_function = minimize_f
                x += z1
                y += z2
                solution_count += 1
    vector = (x, y)
    return [vector, min_function, solution_count]


sp = [[.9, 3.2], [-2.5, 3.2], [4.2, -2], [0, 0]]
p = [30, 120]
z = [0.03, 0.1]

test = RHC(sp[0], p[0], z[0], 5)
print(test)
