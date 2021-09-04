import sys

from factorint.factor import factor, FactorizationMode


def main():
    N = int(sys.argv[1])
    factors = factor(N)
    print(factors)


if __name__ == '__main__':
    main()
