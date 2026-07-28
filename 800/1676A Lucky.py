def solve():
    # Read the number of test cases
    t = int(input())

    # Process each testcase
    for _ in range(t):
        s = input().strip()

        # Calculate the sum of the first 3 digits
        sum_first_half = int(s[0]) + int(s[1]) + int(s[2])

        # Calculate the sum of the last 3 digits
        sum_second_half = int(s[3]) + int(s[4]) + int(s[5])

        # Compare and print result
        if sum_first_half == sum_second_half:
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    solve()