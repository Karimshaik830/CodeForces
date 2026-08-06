def solve():
    # Read the number of test cases
    t = int(input())

    # Process each test case
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        # If the total sum is even, it's possible. Otherwise, it's not.
        if sum(a) % 2 == 0:
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    solve()