# problem: https://pl.spoj.com/problems/ETI06F1/


def splitting(x1):
    x1 = x1.split(" ")
    return float(x1[0]), float(x1[1])


def p_pow(r):
    return 3.141592654 * r


def pitagoras_pow(r, d):
    return r * r - (d / 2) * (d / 2)


def main():
    x1 = input()
    r, d = splitting(x1)
    r_pow = pitagoras_pow(r, d)
    p_m = p_pow(r_pow)
    print(round(p_m, 2))


main()
