def solve():
    n = int(input())
    x = 0
    for _ in range(n):
        stmt = input()
        if '+' in stmt:
            x += 1
        else:
            x -= 1
    print(x)


if __name__ == '__main__':
    solve()