import sys


def solve():
    # Read all inputs at once and split by whitespace for speed
    input_data = sys.stdin.read().split()

    if not input_data:
        return

    # The first number is the number of test cases
    t = int(input_data[0])

    # Process each pair of (a, b)
    # We step by 2 through the list starting from index 1
    for i in range(1, len(input_data), 2):
        a = int(input_data[i])
        b = int(input_data[i + 1])

        # Calculate the remainder
        rem = a % b

        # Print the required moves
        if rem == 0:
            print(0)
        else:
            print(b - rem)


if __name__ == '__main__':
    solve()