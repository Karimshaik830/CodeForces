def solve():
    # Read the total amount of money
    n = int(input())

    bills = 0
    denominations = [100, 20, 10, 5, 1]

    # Greedily take as many large bills as possible
    for denom in denominations:
        bills += n // denom  # Add the number of bills of this denomination
        n %= denom  # Update n to the remaining amount

    # Print the total number of bills
    print(bills)


if __name__ == '__main__':
    solve()