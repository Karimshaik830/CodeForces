def solve():
    # Read the integer n
    n = int(input())

    # If n is even
    if n % 2 == 0:
        print(n // 2)
    # If n is odd
    else:
        # We use integer division // to ensure the output doesn't get a .0 decimal
        print(-(n + 1) // 2)


if __name__ == '__main__':
    solve()