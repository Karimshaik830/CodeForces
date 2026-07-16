def solve():
    # Read the number of test cases
    t = int(input())

    # Process each test case
    for _ in range(t):
        s = input().strip()

        # Convert to uppercase and compare
        if s.upper() == "YES":
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    solve()