# Miller-Rabin test
def is_provable_composite_miller_rabin(n, a):
    if n % 2 == 0:
        return n != 2

    d, s = n - 1, 0
    while d % 2 == 0:
        d, s = d // 2, s + 1

    b = pow(a, d, n)  # pow mod
    if b == 1 or b == n - 1:
        return False

    e = 0
    while e <= s - 2:
        b, e = (b * b) % n, e + 1
        if b == n - 1:
            return False

    return True
