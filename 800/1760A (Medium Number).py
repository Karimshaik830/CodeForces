def solve():
    # Read the number of test cases
    t = int(input())

    # Process each test case
    for _ in range(t):
        # Read the three numbers into a list
        nums = list(map(int, input().split()))

        # Sort the list in ascending order
        nums.sort()

        # The medium number is now in the middle (index 1)
        print(nums[1])


if __name__ == '__main__':
    solve()