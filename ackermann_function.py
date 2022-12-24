def ackermann(m, n):
    if m == 0: return n + 1
    elif m > 0 and n == 0: return ackermann(m - 1, 1)
    elif m > 0 and n > 0: return ackermann(m - 1, ackermann(m, n - 1))

def main():
    print(ackermann(2, 2))

if __name__ == '__main__':
    main()
