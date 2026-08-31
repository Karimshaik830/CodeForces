def solve():
    # Read the integer n
    n = int(input())

    # If n is even, use 4 and n - 4
    if n % 2 == 0:
        print(f"4 {n - 4}")
    # If n is odd, use 9 and n - 9
    else:
        print(f"9 {n - 9}")


if __name__ == '__main__':
    solve()