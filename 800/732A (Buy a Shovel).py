def solve():
    # Read k and r
    k, r = map(int, input().split())

    # Loop from 1 to 10 (inclusive)
    for i in range(1, 11):
        total_cost = i * k

        # Check if it ends in 0 or ends in r
        if total_cost % 10 == 0 or total_cost % 10 == r:
            print(i)
            break


if __name__ == '__main__':
    solve()