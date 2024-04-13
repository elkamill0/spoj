# problem: https://pl.spoj.com/problems/FCTRL3/

'''
 1! =                         1
 2! =                         2
 3! =                         6
 4! =                       2 4
 5! =                     1 2 0
 6! =                     7 2 0
 7! =                   5 0 4 0
 8! =                 4 0 3 2 0
 9! =               3 6 2 8 8 0
10! =             3 6 2 8 8 0 0
11! =           3 9 6 1 6 8 0 0
12! =         4 7 9 0 0 1 6 0 0
15! = 1 3 0 7 6 7 4 3 6 8 0 0 0
'''



def silnia(n):
    sum = 1
    if n >= 10:
        return "0 0"

    for i in range(1, n+1):
        sum *= i
    sum = " ".join(str(sum)[-2:])

    if len(sum) < 3:
        return "0 "+sum

    return(sum)

def main():
    x = int(input())
    for i in range(x):
        x1 = int(input())
        print(silnia(x1))
main()