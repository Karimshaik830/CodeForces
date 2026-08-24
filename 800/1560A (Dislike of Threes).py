def solve():
    # Read the number of test cases
    t = int(input())

    # Process each test case
    for _ in range(t):
        k = int(input())

        count = 0
        i = 1

        # Keep checking numbers until we find the k-th liked one
        while True:
            # Check if it is NOT divisible by 3 AND does NOT end in 3
            if i % 3 != 0 and i % 10 != 3:
                count += 1

                # If we've found the k-th number, print and break
                if count == k:
                    print(i)
                    break

            i += 1


if __name__ == '__main__':
    solve()