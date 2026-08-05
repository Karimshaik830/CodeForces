def solve():
    # Read the number of test cases
    t = int(input())

    # Process each test case
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))

        # If k is anywhere in the list, the answer is YES
        if k in a:
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    solve()