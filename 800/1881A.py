def solve():
    # Read the number of test cases
    t = int(input())

    # Process each test case
    for _ in range(t):
        n, m = map(int, input().split())
        x = input().strip()
        s = input().strip()

        ops = 0
        found = False

        # 6 operations are more than enough for n*m <= 25
        for _ in range(7):
            if s in x:
                print(ops)
                found = True
                break
            # Double the string
            x += x
            ops += 1

        # If it never appeared, it's impossible
        if not found:
            print("-1")


if __name__ == '__main__':
    solve()