import sys


def solve():
    # Read all input from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    t = int(input_data[0])

    # Process each testcase
    for i in range(1, t + 1):
        n_str = input_data[i]
        length = len(n_str)
        ans = []

        # Loop through each digit in the string
        for idx, digit in enumerate(n_str):
            if digit != '0':
                # Calculate how many zeros to append based on the position
                zeros = length - idx - 1
                ans.append(digit + '0' * zeros)

        # Print the number of summands
        print(len(ans))
        # Print the summands separated by spaces
        print(" ".join(ans))


if __name__ == '__main__':
    solve()