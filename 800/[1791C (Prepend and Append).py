def solve():
    # Read the number of test cases
    t = int(input())

    # Process each testcase
    for _ in range(t):
        n = int(input())
        s = input().strip()

        l = 0
        r = n - 1

        # While the ends are different, "undo" the operation
        while l < r and s[l] != s[r]:
            l += 1
            r -= 1

        # The length of the remaining middle part
        print(r - l + 1)


if __name__ == '__main__':
    solve()