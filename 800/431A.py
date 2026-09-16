def solve():
    # Read the calorie values and store them in a list
    a = list(map(int, input().split()))

    # Read the string representing the game process
    s = input().strip()

    total_calories = 0

    # Iterate through the string and add the corresponding calories
    for char in s:
        # Convert character to integer and subtract 1 for 0-based indexing
        index = int(char) - 1
        total_calories += a[index]

    # Print the total calories wasted
    print(total_calories)


if __name__ == '__main__':
    solve()