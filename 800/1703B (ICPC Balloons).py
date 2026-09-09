def solve():
    # Read the number of test cases
    t = int(input())

    # Process each test case
    for _ in range(t):
        n = int(input())
        s = input().strip()

        # Total balloons = total length + number of unique characters
        ans = n + len(set(s))

        print(ans)


if __name__ == '__main__':
    solve()