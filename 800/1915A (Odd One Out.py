def solve():
    # Read the number of test cases
    t = int(input())

    # Process each test case
    for _ in range(t):
        a, b, c = map(int, input().split())

        # Check which two are equal and print the third
        if a == b:
            print(c)
        elif a == c:
            print(b)
        else:
            print(a)


if __name__ == '__main__':
    solve()