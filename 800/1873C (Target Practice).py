def solve():
    # Read the number of test cases
    t = int(input())

    # Process each test case
    for _ in range(t):
        total_score = 0

        # Read the 10x10 grid row by row
        for i in range(10):
            row = input().strip()
            for j in range(10):
                # If there is an arrow, add its point value
                if row[j] == 'X':
                    score = min(i, j, 9 - i, 9 - j) + 1
                    total_score += score

        # Print the total score for this test case
        print(total_score)


if __name__ == '__main__':
    solve()