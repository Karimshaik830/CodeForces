def solve():
    # Read the number of test cases
    t = int(input())

    # Process each test case
    for _ in range(t):
        b = input().strip()

        # Reconstruct 'a' by taking the first character
        # and then every second character of 'b'
        a = b[0] + b[1::2]

        # Print the reconstructed string
        print(a)


if __name__ == '__main__':
    solve()