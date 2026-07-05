def solve():
    # Read the inputs. Each number is on a separate line.
    k = int(input())
    l = int(input())
    m = int(input())
    n = int(input())
    d = int(input())

    damaged_dragons = 0

    # Loop through all dragons from 1 to d
    for i in range(1, d + 1):
        # If the dragon is a multiple of any of the given numbers, it takes damage
        if i % k == 0 or i % l == 0 or i % m == 0 or i % n == 0:
            damaged_dragons += 1

    # Print the total number of damaged dragons
    print(damaged_dragons)


if __name__ == '__main__':
    solve()