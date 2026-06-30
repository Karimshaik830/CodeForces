def solve():
    # Read the input string and immediately convert to lowercase
    s = input().lower()

    # Define our vowels (we can use a string or a set)
    vowels = "aoyeui"
    result = ""

    # Loop through each character in the string
    for char in s:
        # If the character is a consonant
        if char not in vowels:
            result += "." + char

    # Print the final formatted string
    print(result)


if __name__ == '__main__':
    solve()