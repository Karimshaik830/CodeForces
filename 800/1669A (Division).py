def solve():
    # Read the number of test cases
    t = int(input())

    # Process each test case
    for _ in range(t):
        rating = int(input())

        # Check thresholds from top to bottom
        if rating >= 1900:
            print("Division 1")
        elif rating >= 1600:
            print("Division 2")
        elif rating >= 1400:
            print("Division 3")
        else:
            print("Division 4")


if __name__ == '__main__':
    solve()