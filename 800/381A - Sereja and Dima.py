def solve():
    # Read the number of cards
    n = int(input())

    # Read the cards into a list
    cards = list(map(int, input().split()))

    sereja_score = 0
    dima_score = 0

    # Two pointers for the leftmost and rightmost available cards
    left = 0
    right = n - 1

    # Keep track of whose turn it is
    sereja_turn = True

    while left <= right:
        # Determine the larger card on the ends
        if cards[left] > cards[right]:
            picked_card = cards[left]
            left += 1
        else:
            picked_card = cards[right]
            right -= 1

        # Add the picked card to the correct player's score
        if sereja_turn:
            sereja_score += picked_card
        else:
            dima_score += picked_card

        # Switch turns
        sereja_turn = not sereja_turn

    # Print the final scores
    print(f"{sereja_score} {dima_score}")


if __name__ == '__main__':
    solve()