import sys


def solve():
    # Read all input from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    # Number of test cases
    t = int(input_data[0])

    # Process each test case
    for i in range(1, t + 1):
        n = int(input_data[i])

        # If n is divisible by 3, Second wins. Otherwise, First wins.
        if n % 3 == 0:
            print("Second")
        else:
            print("First")


if __name__ == '__main__':
    solve()