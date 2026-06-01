import sys
import math


def solve():
    # Read all inputs at once safely
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    # Parse initial coordinates
    ax, ay, bx, by, tx, ty = map(int, input_data[0:6])
    n = int(input_data[6])

    idx = 7
    total_dist = 0
    A_costs = []
    B_costs = []

    # Process each bottle
    for i in range(n):
        x = int(input_data[idx])
        y = int(input_data[idx + 1])
        idx += 2

        # Distance from bin to bottle
        d_bin = math.hypot(x - tx, y - ty)
        # Add a full round-trip to the base total distance
        total_dist += 2 * d_bin

        # Calculate the cost adjustment if Adil or Bera picks this bottle first
        dA = math.hypot(x - ax, y - ay) - d_bin
        dB = math.hypot(x - bx, y - by) - d_bin

        A_costs.append((dA, i))
        B_costs.append((dB, i))

    # Sort to easily find the top 2 best (most negative) cost adjustments
    A_costs.sort(key=lambda item: item[0])
    B_costs.sort(key=lambda item: item[0])

    ans = float('inf')

    # Scenario 1: Only Adil picks the first bottle
    ans = min(ans, A_costs[0][0])

    # Scenario 2: Only Bera picks the first bottle
    ans = min(ans, B_costs[0][0])

    # Scenario 3: Both Adil and Bera pick a first bottle
    if n > 1:
        if A_costs[0][1] != B_costs[0][1]:
            # They pick different best bottles
            ans = min(ans, A_costs[0][0] + B_costs[0][0])
        else:
            # They conflict on the best bottle! Try the second best for each.
            ans = min(ans, A_costs[0][0] + B_costs[1][0])
            ans = min(ans, A_costs[1][0] + B_costs[0][0])

    # Print with high precision as required by the problem
    print(f"{total_dist + ans:.12f}")


if __name__ == '__main__':
    solve()