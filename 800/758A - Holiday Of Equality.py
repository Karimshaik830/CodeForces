def solve():
    # Read the number of citizens
    n = int(input())

    # Read the welfares into a list
    a = list(map(int, input().split()))

    # Find the maximum welfare
    max_val = max(a)

    # Calculate the total burles needed
    total_spent = sum(max_val - x for x in a)

    # Print the result
    print(total_spent)


if __name__ == '__main__':
    solve()