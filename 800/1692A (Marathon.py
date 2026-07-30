def solve():
    # Read the number of test cases
    t = int(input())

    # Process each test case
    for _ in range(t):
        # Read the four distances
        a, b, c, d = map(int, input().split())

        count = 0

        # Check how many distances are strictly greater than Timur's (a)
        if b > a:
            count += 1
        if c > a:
            count += 1
        if d > a:
            count += 1

        # Print the result
        print(count)


if __name__ == '__main__':
    solve()