def solve():
    # Read the Borze code string
    s = input().strip()

    i = 0
    n = len(s)
    ans = []

    # Process the string from left to right
    while i < n:
        if s[i] == '.':
            ans.append('0')
            i += 1
        elif s[i] == '-':
            # Look ahead at the next character
            if s[i + 1] == '.':
                ans.append('1')
            else:
                ans.append('2')
            # Skip the next character since we just processed it
            i += 2

    # Print the decoded number
    print("".join(ans))


if __name__ == '__main__':
    solve()