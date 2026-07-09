import sys


def solve():
    # Read all inputs at once and split by whitespace
    input_data = sys.stdin.read().split()

    if not input_data:
        return

    # The first number is the number of test cases
    t = int(input_data[0])

    # Process each test case
    for i in range(1, t + 1):
        n = int(input_data[i])

        # Apply the math formula
        print((n - 1) // 2)


if __name__ == '__main__':
    solve()