def solve():
    # Read the number as a string
    s = input().strip()

    # Count the total number of '4's and '7's in the string
    lucky_count = s.count('4') + s.count('7')

    # Check if the count itself is exactly 4 or 7
    if lucky_count == 4 or lucky_count == 7:
        print("YES")
    else:
        print("NO")


solve()