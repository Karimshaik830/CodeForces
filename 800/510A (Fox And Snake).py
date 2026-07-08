def solve():
    # Read n and m
    n, m = map(int, input().split())

    # Loop through the rows from 1 to n
    for i in range(1, n + 1):
        if i % 2 != 0:
            # Odd rows: full line of hashes
            print("#" * m)
        elif i % 4 == 2:
            # Row 2, 6, 10...: dots then a hash
            print("." * (m - 1) + "#")
        elif i % 4 == 0:
            # Row 4, 8, 12...: a hash then dots
            print("#" + "." * (m - 1))


if __name__ == '__main__':
    solve()