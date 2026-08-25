def solve():
    # Read the number of test cases
    t = int(input())

    # Process each test case
    for _ in range(t):
        a, b = input().split()

        # Create the new strings by swapping the first characters
        new_a = b[0] + a[1:]
        new_b = a[0] + b[1:]

        # Print the result
        print(f"{new_a} {new_b}")


if __name__ == '__main__':
    solve()