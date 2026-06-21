def solve():
    # Read the 4 integers, split them into a list, and convert the list to a set
    unique_colors = set(input().split())

    # He needs 4 unique colors total. We subtract the unique ones he already has.
    print(4 - len(unique_colors))


if __name__ == '__main__':
    solve()