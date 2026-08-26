def solve():
    # Read the number of test cases
    t = int(input())

    # Process each testcase
    for _ in range(t):
        s = input().strip()

        # Check if at least one character is in its correct original position
        if s[0] == 'a' or s[1] == 'b' or s[2] == 'c':
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    solve()