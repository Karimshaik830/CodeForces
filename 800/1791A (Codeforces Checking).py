def solve():
    # Read the number of test cases
    t = int(input())

    # Define the target string
    target = "codeforces"

    # Process each test case
    for _ in range(t):
        c = input().strip()

        # Check if the character is in the target string
        if c in target:
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    solve()