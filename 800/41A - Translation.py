import sys


def solve():
    # Read all inputs safely, splitting by any whitespace/newlines
    input_data = sys.stdin.read().split()

    # Safety check: ensure we actually read two strings
    if len(input_data) < 2:
        return

    s = input_data[0]
    t = input_data[1]

    # s[::-1] creates a reversed copy of the string s
    # Check if the reversed 's' perfectly matches 't'
    if s[::-1] == t:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    solve()