def solve():
    # Read the number of test cases
    t = int(input())

    # Process each test case
    for _ in range(t):
        n = int(input())
        k = n // 2

        # If k is odd, it's impossible
        if k % 2 != 0:
            print("NO")
        else:
            print("YES")

            # Construct the even half
            evens = [2 * i for i in range(1, k + 1)]

            # Construct the odd half (all but the last element)
            odds = [2 * i - 1 for i in range(1, k)]

            # Add the final odd element to balance the sums
            odds.append(3 * k - 1)

            # Print the complete array
            print(*(evens + odds))


if __name__ == '__main__':
    solve()