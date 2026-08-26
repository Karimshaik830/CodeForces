def solve():
    # Read the number of children
    n = int(input())

    # Read the skills
    t = list(map(int, input().split()))

    # Lists to store the 1-based indices for each skill
    prog = []
    math = []
    pe = []

    # Group the indices
    for i in range(n):
        if t[i] == 1:
            prog.append(i + 1)
        elif t[i] == 2:
            math.append(i + 1)
        else:
            pe.append(i + 1)

    # The max number of teams is limited by the smallest group
    w = min(len(prog), len(math), len(pe))

    # Print the number of teams
    print(w)

    # Print the indices of the children for each team
    for i in range(w):
        print(f"{prog[i]} {math[i]} {pe[i]}")


if __name__ == '__main__':
    solve()