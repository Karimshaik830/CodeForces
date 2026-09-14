def solve():
    # Read the number of test cases
    t = int(input())

    # Sort the target string once to compare against
    target = sorted("Timur")

    # Process each test case
    for _ in range(t):
        n = int(input())
        s = input().strip()

        # Check if length is 5 and the sorted characters match
        if n == 5 and sorted(s) == target:
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    solve()