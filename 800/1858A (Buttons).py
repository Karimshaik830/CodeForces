def solve():
    # Read the number of test cases
    t = int(input())

    # Process each test case
    for _ in range(t):
        a, b, c = map(int, input().split())

        # If c is odd, Anna gets an extra turn from the shared pool
        if c % 2 == 1:
            a += 1

        # Check who has more turns available
        if a > b:
            print("First")
        else:
            print("Second")


if __name__ == '__main__':
    solve()