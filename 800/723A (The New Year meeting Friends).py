def solve():
    # Read the three coordinates and put them into a list
    coords = list(map(int, input().split()))

    # The minimum total distance is simply the maximum minus the minimum
    print(max(coords) - min(coords))


if __name__ == '__main__':
    solve()