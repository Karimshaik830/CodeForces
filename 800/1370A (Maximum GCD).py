def solve():
    # Read the number of test cases
    t = int(input())

    # Process each test case
    for _ in range(t):
        n = int(input())

        # The maximum GCD is simply n divided by 2 (rounded down)
        print(n // 2)


if __name__ == '__main__':
    solve()