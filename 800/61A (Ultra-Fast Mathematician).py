def solve():
    # Read the two binary strings
    s1 = input().strip()
    s2 = input().strip()

    result = ""

    # Iterate through the strings character by character
    for i in range(len(s1)):
        # If the digits are different, append '1', otherwise append '0'
        if s1[i] != s2[i]:
            result += "1"
        else:
            result += "0"

    # Print the resulting binary string
    print(result)


if __name__ == '__main__':
    solve()