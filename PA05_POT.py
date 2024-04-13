# problem: https://pl.spoj.com/problems/PA05_POT/

'''
for 1: 1,...

2^1 = 2
2^2 = 4
2^3 = 8
2^4 = 16
2^5 = 32
2^6 = 64
2^7 = 128
2^8 = 256
for 2: 2,4,8,6,...

3^1 = 3
3^2 = 9
3^3 = 27
3^4 = 81
3^5 = 243
3^6 = 729
for 3: 3,9,7,1...

4^1 = 4
4^2 = 16
4^3 = 64
4^4 = 256
for 4: 4,6,...

5^1 = 5
5^2 = 25
5^3 = 125
for 5: 5,...

6^1 = 6
6^2 = 36
6^3 = 216
for 6: 6,...

7^1 = 7
7^2 = 49
7^3 = 343
7^4 = 2401
7^5 = 16807
7^6 = 117649
for 7: 7,9,3,1,...

8^1 = 8
8^2 = 64
8^3 = 512
8^4 = 4096
8^5 = 32768
for 8: 8,4,2,6,...

9^1 = 9
9^2 = 81
9^3 = 729
9^4 = 6561
for 9: 9,1,...

10^1 = 10
10^2 = 100
for 10: 0,...

11^1 = 11
11^2 = 121
11^3 = 1331

for 11: 1

12^1 = 12
12^2 = 144
12^3 = 1728
12^4 = 20736
for 12: 2,4,8,6,...

'''


def loader(x):
    x = x.split(" ")
    return x[0], x[1]


def result(b, tab):
    b = b - 1
    return tab[b % len(tab)]


def main():
    x = int(input())
    for i in range(x):
        x1 = input()
        a, b = loader(x1)
        a = int(a[-1:])
        b = int(b)
        if b == 0:
            print(1)
        elif a == 0:
            print(0)
        elif a == 1:
            print(1)
        elif a == 2:
            print(result(b, [2, 4, 8, 6]))
        elif a == 3:
            print(result(b, [3, 9, 7, 1]))
        elif a == 4:
            print(result(b, [4, 6]))
        elif a == 5:
            print(5)
        elif a == 6:
            print(6)
        elif a == 7:
            print(result(b, [7, 9, 3, 1]))
        elif a == 8:
            print(result(b, [8, 4, 2, 6]))
        elif a == 9:
            print(result(b, [9, 1]))

main()
