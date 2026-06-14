def solve():
    # Read the number of people (we don't strictly need to use this variable)
    n = input()

    # Read the responses and split them into a list
    responses = input().split()

    # Check if '1' is anywhere in the list of responses
    if '1' in responses:
        print("HARD")
    else:
        print("EASY")


if __name__ == '__main__':
    solve()