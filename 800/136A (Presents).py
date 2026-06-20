def solve():
    # Read the number of friends
    n = int(input())

    # Read who everyone gave gifts to
    p = list(map(int, input().split()))

    # Create a result array filled with 0s.
    # We make it size n + 1 so we can safely use 1-based indexing.
    ans = [0] * (n + 1)

    # Loop through the given array
    # enumerate(p, 1) gives us pairs of (giver, receiver), starting the giver at 1
    for giver, receiver in enumerate(p, 1):
        ans[receiver] = giver

    # Print the result array, skipping the 0th index and unpacking with *
    print(*(ans[1:]))


if __name__ == '__main__':
    solve()