def solve():
    # Read the number of test cases
    t = int(input())

    # Process each test case
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        # Determine the common element
        if a[0] == a[1]:
            common = a[0]
        elif a[0] == a[2]:
            common = a[0]
        else:
            common = a[1]

        # Find the unique element and print its 1-based index
        for i in range(n):
            if a[i] != common:
                print(i + 1)
                break


if __name__ == '__main__':
    solve()