def solve():
    # Read the number of test cases
    t = int(input())

    # Store the unique characters we need
    target_set = set("Timur")

    # Process each test case
    for _ in range(t):
        n = int(input())
        s = input().strip()

        # Check if the length is exactly 5 and all required characters are present
        if n == 5 and set(s) == target_set:
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    solve()