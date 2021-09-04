def iroot(x, n):
    """Finds the integer component of the n'th root of x,
    an integer such that y ** n <= x < (y + 1) ** n.
    """
    high = 1
    while high ** n <= x:
        high *= 2
    low = high // 2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid ** n < x:
            low = mid
        elif high > mid and mid ** n > x:
            high = mid
        else:
            return mid
    return mid + 1


def isqrt(n):
    y, x = n, n + 1
    while y < x:
        x = y
        y = (x + n // x) >> 1
    return x


def ilog2(n):
    return n.bit_length() - 1


def is_perfect_square(n):
    x = isqrt(n)
    return x * x == n


def jacobi(n, k):
    assert (k > 0 and k % 2 == 1)
    n = n % k
    t = 1
    while n != 0:
        while n % 2 == 0:
            n = n // 2
            r = k % 8
            if r == 3 or r == 5:
                t = -t
        n, k = k, n
        if n % 4 == 3 and k % 4 == 3:
            t = -t
        n = n % k
    if k == 1:
        return t
    else:
        return 0


def get_perfect_power(n):
    for b in range(2, ilog2(n)):
        root = iroot(n, b)
        if root ** b == n:
            return root, b
    return n, 1
