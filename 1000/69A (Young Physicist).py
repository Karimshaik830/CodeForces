def solve():
    # Read the number of vectors
    n = int(input())

    sum_x = 0
    sum_y = 0
    sum_z = 0

    # Process each force vector
    for _ in range(n):
        x, y, z = map(int, input().split())
        sum_x += x
        sum_y += y
        sum_z += z

    # Check if all coordinate sums are exactly 0
    if sum_x == 0 and sum_y == 0 and sum_z == 0:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    solve()