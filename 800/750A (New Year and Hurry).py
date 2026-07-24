def solve():
    # Read n (total problems) and k (minutes needed to commute)
    n, k = map(int, input().split())

    # Calculate the total time Limak has for solving problems
    time_left = 240 - k
    solved = 0

    # Try to solve problems from 1 up to n
    for i in range(1, n + 1):
        time_needed = 5 * i

        # If he has enough time to solve this problem
        if time_left >= time_needed:
            time_left -= time_needed
            solved += 1
        else:
            # Not enough time for this or any harder problems
            break

    # Print the total number of problems solved
    print(solved)


if __name__ == '__main__':
    solve()