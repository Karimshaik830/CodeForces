import sys


def solve():
    # Read all input from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    # The first number is the number of test cases
    t = int(input_data[0])

    # Process each test case
    idx = 1
    for _ in range(t):
        n = int(input_data[idx])
        a = int(input_data[idx + 1])
        b = int(input_data[idx + 2])
        idx += 3

        # Apply the logic
        if (a == n and b == n) or (a + b <= n - 2):
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    solve()