def solve():
    # Read the number of test cases
    t = int(input())

    # Process each testcase
    for _ in range(t):
        a, b = map(int, input().split())

        # The expression (c - a) + (b - c) always simplifies to b - a
        print(b - a)


if __name__ == '__main__':
    solve()