def solve():
    # Read k (cost of 1st banana), n (initial dollars), w (number of bananas)
    k, n, w = map(int, input().split())

    # Calculate the total cost using the sum formula
    # We use integer division // to keep it as an integer
    total_cost = k * (w * (w + 1)) // 2

    # The amount to borrow is the cost minus his money, with a minimum of 0
    borrow = max(0, total_cost - n)

    # Print the result
    print(borrow)


if __name__ == '__main__':
    solve()