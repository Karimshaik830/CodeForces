def solve():
    # Read the number of test cases
    t = int(input())

    # Process each test case
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        # Sort the array
        a.sort()

        possible = True

        # Check differences between adjacent elements
        for i in range(1, n):
            if a[i] - a[i - 1] > 1:
                possible = False
                break

        # Print the result
        if possible:
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    solve()