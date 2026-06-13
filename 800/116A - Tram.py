def solve():
    # Read the number of stops
    n = int(input())

    current_passengers = 0
    max_capacity = 0

    # Loop through each stop
    for _ in range(n):
        # Read the number of exiting (a) and entering (b) passengers
        a, b = map(int, input().split())

        # Update the current number of passengers in the tram
        current_passengers -= a
        current_passengers += b

        # Update the maximum capacity needed so far
        if current_passengers > max_capacity:
            max_capacity = current_passengers

    # Print the highest number of passengers that were in the tram at once
    print(max_capacity)


if __name__ == '__main__':
    solve()