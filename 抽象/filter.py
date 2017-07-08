from math import sqrt


def prime(n):
    if n == 1:
        return True
    for i in range(2, int(sqrt(n) + 1)):
        if (n % i) == 0:
            return True
    return False


print filter(prime, range(100))
