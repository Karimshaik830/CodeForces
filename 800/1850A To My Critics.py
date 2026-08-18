def solve():
    # Read the number of test cases
    t = int(input())

    # Process each test case
    for _ in range(t):
        a, b, c = map(int, input().split())

        # Check all three possible pairs
        if a + b >= 10:
            print("YES")
        elif a + c >= 10:
            print("YES")
        elif b + c >= 10:
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    solve()