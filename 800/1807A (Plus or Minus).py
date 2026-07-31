def solve():
    # Read the number of test cases
    t = int(input())

    # Process each test case
    for _ in range(t):
        # Read a, b, and c
        a, b, c = map(int, input().split())

        # Check which equation is correct
        if a + b == c:
            print("+")
        else:
            print("-")


if __name__ == '__main__':
    solve()