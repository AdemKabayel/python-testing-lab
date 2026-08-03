def is_prime(n): # asal sayilar
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        # for i range(2, math.isqrt(n)+ 1) same above ⬆️
        if n % i == 0:
            return False
    return True


def is_prime_2(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5)+ 1):
        if n % i  == 0:
            return False
    return True