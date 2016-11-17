def collatz(n):
    print(n)
    if n % 2 == 0:
        collatz(n / 2)
    elif n != 1.0:
        collatz(3 * n + 1)
