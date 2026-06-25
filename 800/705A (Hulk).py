def solve():
    # Read the number of layers
    n = int(input())

    feelings = []

    # Loop from 1 up to n
    for i in range(1, n + 1):
        if i % 2 != 0:  # Odd index
            feelings.append("I hate")
        else:  # Even index
            feelings.append("I love")

    # Join all the feelings with " that " and finish with " it"
    result = " that ".join(feelings) + " it"
    print(result)


if __name__ == '__main__':
    solve()