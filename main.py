import sys
import decimal
sys.stdin = open("input.txt", "rt", encoding="UTF-8")
sys.stdout = open("output.txt", "wt", encoding="UTF-8")


def main():
    decimal.getcontext().prec = 100000

    n = sys.stdin.readline().strip()
    n = decimal.Decimal(n)
    result = n + 1
    print(result)


main()
