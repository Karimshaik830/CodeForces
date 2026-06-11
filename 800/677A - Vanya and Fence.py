def solve():
    # Read n (number of friends) and h (height of the fence)
    n, h = map(int, input().split())

    # Read the heights of the friends into a list
    heights = list(map(int, input().split()))

    total_width = 0

    # Calculate the total width required
    for height in heights:
        if height > h:
            total_width += 2
        else:
            total_width += 1

    # Print the final result
    print(total_width)


if __name__ == '__main__':
    solve()