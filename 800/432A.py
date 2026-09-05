def solve():
    # Read n and k
    n, k = map(int, input().split())

    # Read the participation counts
    y = list(map(int, input().split()))

    # Count how many students are eligible to participate k more times
    valid_students = 0
    for participations in y:
        if participations + k <= 5:
            valid_students += 1

    # Each team needs exactly 3 students
    print(valid_students // 3)


if __name__ == '__main__':
    solve()