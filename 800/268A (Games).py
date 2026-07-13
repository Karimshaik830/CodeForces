def solve():
    # Read the number of teams
    n = int(input())

    # Lists to store the home and guest colors
    home_colors = []
    guest_colors = []

    # Read the uniform colors for each team
    for _ in range(n):
        h, a = map(int, input().split())
        home_colors.append(h)
        guest_colors.append(a)

    count = 0

    # Compare every host team against every guest team
    for i in range(n):
        for j in range(n):
            # If the host's home color matches the guest's guest color
            if home_colors[i] == guest_colors[j]:
                count += 1

    # Print the total number of times the host wears their guest uniform
    print(count)


if __name__ == '__main__':
    solve()