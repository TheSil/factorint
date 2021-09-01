from factorint.utils import jacobi


def is_lucas_pseudoprime(n, D):
    # delta(n) = n - (D/n) = d*2^s
    d = n - jacobi(D, n)
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    # computing U_d, V_d
    bits = []
    while d != 0:
        bits.append(d & 1)
        d >>= 1

    U, V = 1, 1
    inv_2 = (n + 1) // 2  # 1/2 mod n
    k = 1
    for b in reversed(bits[:-1]):
        # U2k = Uk * Vk, V2k = (Vk^2+DUk^2)/2
        U, V = (U * V) % n, ((V * V + D * U * U) * inv_2) % n
        k *= 2

        if b == 1:
            # U2k+1 = (P*U2k+V2k)/2, V2k+1 = (DU2k+P*V2k)/2, P=1
            U, V = ((U + V) * inv_2) % n, ((D * U + V) * inv_2) % n
            k = k + 1

    # U_d = 0 mod n
    if U == 0:
        return True

    # V d2^r = 0 mod n
    for r in range(s):
        if V == 0:
            return True

        # U2k = Uk * Vk, V2k = (Vk^2+DUk^2)/2
        U, V = (U * V) % n, ((V * V + D * U * U) * inv_2) % n

    return False
