def solve():
    # Read the coordinate of the friend's house
    x = int(input())

    # Calculate the minimum number of steps
    steps = (x + 4) // 5

    # Print the result
    print(steps)


if __name__ == '__main__':
    solve()