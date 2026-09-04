def solve():
    # Read the number of test cases
    t = int(input())

    # Process each test case
    for _ in range(t):
        a, b, c = map(int, input().split())

        # Check for stair
        if a < b and b < c:
            print("STAIR")
        # Check for peak
        elif a < b and b > c:
            print("PEAK")
        # Otherwise, neither
        else:
            print("NONE")


if __name__ == '__main__':
    solve()