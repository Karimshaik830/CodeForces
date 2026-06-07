def solve():
    # Read n (the starting number) and k (the number of operations)
    n, k = map(int, input().split())

    # Perform the operation exactly k times
    for _ in range(k):
        # Check the last digit using modulo 10
        if n % 10 != 0:
            n -= 1
        else:
            n //= 10  # Integer division to drop the zero

    # Print the final result
    print(n)


if __name__ == '__main__':
    solve()