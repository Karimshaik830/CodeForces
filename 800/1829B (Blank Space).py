def solve():
    # Read the number of test cases
    t = int(input())

    # Process each test case
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        max_zeros = 0
        current_zeros = 0

        # Iterate through the array elements
        for num in a:
            if num == 0:
                # We found a zero, increase our current streak
                current_zeros += 1
                # Update the maximum streak found so far
                max_zeros = max(max_zeros, current_zeros)
            else:
                # We found a one, the zero-streak is broken
                current_zeros = 0

        print(max_zeros)


if __name__ == '__main__':
    solve()