def solve():
    # Read the number of contests
    n = int(input())

    # Read the scores into a list
    scores = list(map(int, input().split()))

    if n == 0:
        print(0)
        return

    amazing_count = 0

    # The first contest sets the baseline
    min_score = scores[0]
    max_score = scores[0]

    # Loop through the rest of the scores
    for i in range(1, n):
        if scores[i] > max_score:
            amazing_count += 1
            max_score = scores[i]
        elif scores[i] < min_score:
            amazing_count += 1
            min_score = scores[i]

    # Print the total number of amazing performances
    print(amazing_count)


if __name__ == '__main__':
    solve()