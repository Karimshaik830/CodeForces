def solve():
    import sys
    input = sys.stdin.read
    data = input().split()

    if not data:
        return

    t = int(data[0])

    # Process each test case
    for i in range(1, 2 * t, 2):
        a = int(data[i])
        b = int(data[i + 1])

        # Calculate absolute difference
        diff = abs(a - b)

        # Ceiling division by 10
        print((diff + 9) // 10)


if __name__ == '__main__':
    solve()