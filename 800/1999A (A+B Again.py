def solve():
    # Read the number of test cases
    t = int(input())

    # Process each testcase
    for _ in range(t):
        n = int(input())

        # Calculate and print the sum of the digits
        print((n // 10) + (n % 10))


if __name__ == '__main__':
    solve()