def solve():
    # Read the length of the string (we actually don't need to use this variable)
    n = int(input())

    # Read the string
    s = input().strip()

    # Convert to lowercase, put in a set to remove duplicates, and check length
    if len(set(s.lower())) == 26:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    solve()