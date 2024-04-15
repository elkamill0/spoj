# problem: https://pl.spoj.com/problems/RNO_DOD/


def loader(z):
    z = z.split(" ")
    return list(map(int, z))


def main():
    x = int(input())

    for i in range(x):
        y = int(input())
        z = input()
        print(sum(loader(z)))


main()