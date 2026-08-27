def solve():
    # Define the target string
    target = "codeforces"

    # Read the number of test cases
    t = int(input())

    # Process each test case
    for _ in range(t):
        s = input().strip()

        diff_count = 0

        # Compare character by character
        for i in range(10):
            if s[i] != target[i]:
                diff_count += 1

        # Print the total number of differences
        print(diff_count)


if __name__ == '__main__':
    solve()