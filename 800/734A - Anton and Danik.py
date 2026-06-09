def solve():
    # Read the number of games (we don't actually need to use this variable)
    n = int(input())

    # Read the string of game outcomes
    s = input().strip()

    # Count the wins for each player
    anton_wins = s.count('A')
    danik_wins = s.count('D')

    # Compare and print the winner
    if anton_wins > danik_wins:
        print("Anton")
    elif danik_wins > anton_wins:
        print("Danik")
    else:
        print("Friendship")


if __name__ == '__main__':
    solve()