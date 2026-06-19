def solve():
    # Read the number of drinks
    n = int(input())

    # Read the percentages into a list
    p = list(map(int, input().split()))

    # Calculate the average
    average = sum(p) / n

    # Print the result.
    # We can format it to 12 decimal places to be completely safe with precision.
    print(f"{average:.12f}")


if __name__ == '__main__':
    solve()