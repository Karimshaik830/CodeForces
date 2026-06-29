def solve():
    # Read n, m, and a
    n, m, a = map(int, input().split())

    # Calculate the number of stones for length and width rounding up
    length_stones = (n + a - 1) // a
    width_stones = (m + a - 1) // a

    # Print the total number of stones
    print(length_stones * width_stones)


if __name__ == '__main__':
    solve()