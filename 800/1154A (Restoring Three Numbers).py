def solve():
    # Read the four numbers into a list
    nums = list(map(int, input().split()))

    # Sort the list so the largest number (a+b+c) is at the end
    nums.sort()

    # The largest number is at index 3
    total_sum = nums[3]

    # Calculate a, b, and c
    a = total_sum - nums[0]
    b = total_sum - nums[1]
    c = total_sum - nums[2]

    # Print the result
    print(f"{a} {b} {c}")


if __name__ == '__main__':
    solve()