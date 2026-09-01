def solve():
    # Read the rolls of Yakko and Wakko
    y, w = map(int, input().split())

    # Find the maximum of the two rolls
    m = max(y, w)

    # Calculate the number of winning outcomes for Dot
    outcomes = 6 - m + 1

    # Pre-calculated irreducible fractions for 0 to 6 outcomes
    # (Index 0 is empty since outcomes will be at least 1)
    fractions = ["", "1/6", "1/3", "1/2", "2/3", "5/6", "1/1"]

    # Print the result
    print(fractions[outcomes])

if __name__ == '__main__':
    solve()