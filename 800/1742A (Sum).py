def solve():
    # Read the number of test cases
    t = int(input())

    # Process each test case
    for _ in range(t):
        # Read a, b, and c
        a, b, c = map(int, input().split())

        # Check all three possibilities
        if a + b == c or a + c == b or b + c == a:
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    solve()