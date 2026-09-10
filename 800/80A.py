def is_prime(num):
    # Check if a number is prime
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def solve():
    # Read the two integers
    n, m = map(int, input().split())

    # Start looking for the next prime right after n
    next_prime = n + 1

    # Keep incrementing until we hit a prime number
    while not is_prime(next_prime):
        next_prime += 1

    # Check if the next prime is exactly m
    if next_prime == m:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    solve()