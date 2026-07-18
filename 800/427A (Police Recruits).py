def solve():
    # Read the number of events
    n = int(input())

    # Read all events into a list
    events = list(map(int, input().split()))

    officers = 0
    untreated = 0

    # Process each event chronologically
    for event in events:
        if event == -1:
            # A crime occurred
            if officers > 0:
                officers -= 1  # An officer investigates
            else:
                untreated += 1  # No officer available, goes untreated
        else:
            # Recruits are hired
            officers += event

    # Print the total number of untreated crimes
    print(untreated)


if __name__ == '__main__':
    solve()