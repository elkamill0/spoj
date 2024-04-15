# problem: https://pl.spoj.com/problems/PP0504B/


def splitting(x1):
    x1 = x1.split(" ")
    return x1[0], x1[1]


def main():
    x = int(input())
    for i in range(x):
        x1 = input()
        a, b = splitting(x1)
        stop = len(b) if len(a) > len(b) else len(a)
        final_string = ""
        for j in range(stop):
            final_string += a[j] + b[j]
        print(final_string)


main()
