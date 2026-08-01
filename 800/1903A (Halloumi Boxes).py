def solve():
    # Read the number of test cases
    t = int(input())

    # Process each test case
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))

        # If k >= 2, we can always sort it.
        # If k == 1, it must already be sorted.
        if k >= 2 or a == sorted(a):
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    solve()