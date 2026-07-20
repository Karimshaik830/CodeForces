def solve():
    # Read all 8 variables from the input line
    n, k, l, c, d, p, nl, np = map(int, input().split())

    # Calculate total toasts possible for each ingredient
    drink_toasts = (k * l) // nl
    lime_toasts = c * d
    salt_toasts = p // np

    # Find the limiting ingredient (the bottleneck)
    total_toasts = min(drink_toasts, lime_toasts, salt_toasts)

    # Divide the total toasts by the number of friends
    print(total_toasts // n)


if __name__ == '__main__':
    solve()