def solve():
    # Read the number of red and blue socks
    a, b = map(int, input().split())

    # Days with different socks is the minimum of the two
    different_socks = min(a, b)

    # Remaining socks of the same color can form pairs by dividing by 2
    same_socks = abs(a - b) // 2

    # Print the result
    print(f"{different_socks} {same_socks}")


if __name__ == '__main__':
    solve()