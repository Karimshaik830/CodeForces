def solve():
    # Read the number of rooms
    n = int(input())

    available_rooms = 0

    # Loop through each room
    for _ in range(n):
        # Read current occupants (p) and max capacity (q)
        p, q = map(int, input().split())

        # Check if there is room for at least 2 more people
        if q - p >= 2:
            available_rooms += 1

    # Print the final count
    print(available_rooms)


if __name__ == '__main__':
    solve()