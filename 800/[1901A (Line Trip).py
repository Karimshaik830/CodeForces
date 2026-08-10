def solve():
    # Read the number of test cases
    t = int(input())

    # Process each test case
    for _ in range(t):
        n, x = map(int, input().split())
        a = list(map(int, input().split()))

        # 1. Distance from start to the first station
        max_diff = a[0]

        # 2. Distances between consecutive stations
        for i in range(1, n):
            max_diff = max(max_diff, a[i] - a[i - 1])

        # 3. Distance from the last station to x and back
        max_diff = max(max_diff, 2 * (x - a[-1]))

        # Print the maximum distance required
        print(max_diff)


if __name__ == '__main__':
    solve()