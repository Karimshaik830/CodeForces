def solve():
    # Read n (number of children) and t (seconds)
    n, t = map(int, input().split())

    # Read the initial queue arrangement
    s = input().strip()

    # For each second, replace all occurrences of "BG" with "GB"
    for _ in range(t):
        s = s.replace("BG", "GB")

    # Print the final arrangement
    print(s)


if __name__ == '__main__':
    solve()