def solve():
    # Read the entire line of input
    s = input()

    unique_letters = set()

    # Loop through each character in the string
    for char in s:
        # Python's .isalpha() checks if the character is a letter
        if char.isalpha():
            unique_letters.add(char)

    # Print the number of unique letters
    print(len(unique_letters))


if __name__ == '__main__':
    solve()