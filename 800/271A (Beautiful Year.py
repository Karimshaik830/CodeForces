def solve():
    # Read the initial year
    y = int(input())

    # Start looking at the strictly next year
    y += 1

    # Loop until we find a year with 4 distinct digits
    # Converting the number to a string, then to a set, removes duplicates
    while len(set(str(y))) < 4:
        y += 1

    # Print the beautiful year
    print(y)


if __name__ == '__main__':
    solve()