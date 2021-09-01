def is_composite_miller_rabin(n, a):
    if n % 2 == 0:
        return True

    d = n - 1
    s = 0
    while d > 0:
        d //= 2
        s += 1

    b = pow(a, d, n)  # pow mod
    if b == 1:
        return False

    e = 0
    while b != n - 1 and e <= s - 2:
        b = (b * b) % n
        e += 1
        if b != n - 1:
            return True

    return False
