# problem: https://pl.spoj.com/problems/PRIME_T/

def prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:  # nie ma sensu dzielić przez większą liczbę niż potęga, ponieważ będzie się ona powtarzać
        if n % i == 0:
            return False
        i += 1
    return True

def main():
    x = int(input())
    for i in range(x):
        x1 = int(input())
        print("TAK" if prime(x1) else "NIE")    # Jeżeli jest pierwsza, wypisz "TAK", w przeciwnym wypadku - "NIE"
main()
