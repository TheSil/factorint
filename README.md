# factorint
Python integer factorization library. Intended mainly for my personal study of factorization algorithms (for now).

Only simplest, naive algorithms implemented for now:
- Checking divisibility by small primes
- Checking for perfect powers
- Pollard Rho factorization
- Baillie–PSW primality test for probable prime testing (faster than trying to factor)

Example:

```Python
from factorint.factor import factor

factor(123456789123456789123456789123456789)
```

Output:
```
[3^2, 7, 11, 13, 19, 101, 3607, 3803, 9901, 52579, 999999000001]
```

If we are fine even with partial factorization or with first factor, we can use:
```Python
from factorint.factor import factor, FactorizationMode

factor(123434342131345364563456789123456789, mode=FactorizationMode.PartialFactorization)
```

Output:
```
[29, 13487, COMP(315589577016297595803511399543)]
```

More detailed output can be generated using the `verbose` flag:

```Python
factor(100000980001501, verbose=True)
```

Output:
```
INFO:factorint:factoring: 100000980001501
INFO:factorint:checking for small prime factors
INFO:factorint:checking factor: 100000980001501
INFO:factorint:running alg: check_perfect_power
INFO:factorint:running alg: check_prime_baillie_psw
INFO:factorint:running alg: find_by_pollard_rho
INFO:factorint:found factor: 10000079
INFO:factorint:found factor: 10000019
INFO:factorint:checking factor: 10000079
INFO:factorint:running alg: check_perfect_power
INFO:factorint:running alg: check_prime_baillie_psw
INFO:factorint:found prime factor: 10000079
INFO:factorint:checking factor: 10000019
INFO:factorint:running alg: check_perfect_power
INFO:factorint:running alg: check_prime_baillie_psw
INFO:factorint:found prime factor: 10000019
INFO:factorint:found prime factors: [10000079, 10000019]
INFO:factorint:remaining factors: []
INFO:factorint:checked all primes up to: 499979
[10000079, 10000019]
```

TODO - Python:
- update to structure to importable/installable package
- argparse for factor cli
- formalize configurable parameters for each algorithm

TODO - algorithms:
- Continued fraction factorization
- Quadratic sieve factorization
- Number Field sieve factorization
