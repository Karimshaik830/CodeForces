import sys


def solve():
    # Read all input data at once and split by whitespace
    data = sys.stdin.read().split()

    # Safety check: if input is empty, just exit
    if not data:
        return

    n = int(data[0])

    if n == 0:
        print(0)
        return

    groups = 1

    # Loop starting from the second magnet (index 2 in our data list)
    for i in range(2, n + 1):
        # If this magnet is different from the previous one, a new group starts
        if data[i] != data[i - 1]:
            groups += 1

    # Print the total number of groups
    print(groups)


if __name__ == '__main__':
    solve()