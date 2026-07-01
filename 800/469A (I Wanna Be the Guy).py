def solve():
    # Read the total number of levels
    n = int(input())

    # Read X and Y's data, split by space, and convert to integers
    x_data = list(map(int, input().split()))
    y_data = list(map(int, input().split()))

    # Slice off the first element (the count) and combine the rest into a set
    passed_levels = set(x_data[1:] + y_data[1:])

    # Check if the number of unique levels they can pass equals n
    if len(passed_levels) == n:
        print("I become the guy.")
    else:
        print("Oh, my keyboard!")


if __name__ == '__main__':
    solve()