def solve():
    # Read the number of soldiers
    n = int(input())

    # Read the heights into a list
    a = list(map(int, input().split()))

    max_idx = 0
    min_idx = 0

    # Find the index of the first max and the last min
    for i in range(n):
        if a[i] > a[max_idx]:
            max_idx = i
        # Notice the <= here! It ensures we get the LAST minimum if there's a tie
        if a[i] <= a[min_idx]:
            min_idx = i

    # Calculate the total swaps
    swaps = max_idx + (n - 1 - min_idx)

    # If their paths cross, subtract 1
    if max_idx > min_idx:
        swaps -= 1

    # Print the minimum number of seconds (swaps)
    print(swaps)


if __name__ == '__main__':
    solve()