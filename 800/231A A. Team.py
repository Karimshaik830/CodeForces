def solve():
    # Read the number of problems
    n = int(input())

    implemented_problems = 0

    # Loop through each problem
    for _ in range(n):
        # Read the certainty of Petya, Vasya, and Tonya
        p, v, t = map(int, input().split())

        # If the sum of their certainties is at least 2, they solve it
        if p + v + t >= 2:
            implemented_problems += 1

    # Print the final count
    print(implemented_problems)


if __name__ == '__main__':
    solve()