def build_i(num):
    i = set()
    for lambdaValue in num:
        if 78 > lambdaValue >= -50:
            i.add(8 * lambdaValue + abs(lambdaValue))
    return i


def calc_beta(input_set, I):
    delta = input_set | I
    E = I | delta

    return len(delta) + sum([e**3 for e in E])


input_set = {97, -30, 38, -57, 70, -19, -15, 51, -73, 31}
I = build_i(input_set)
print(calc_beta(input_set, I))

input_set2 = {-61, -93, -87, -22, 17, -40, 26, 59, -2}
I = build_i(input_set2)
print(calc_beta(input_set2, I))
