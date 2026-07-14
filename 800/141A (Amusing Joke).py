def solve():
    # Read the three strings
    guest = input().strip()
    host = input().strip()
    pile = input().strip()

    # Combine the names of the guest and the host
    combined = guest + host

    # Sort both strings and compare them
    if sorted(combined) == sorted(pile):
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    solve()