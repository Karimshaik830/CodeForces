def solve():
    # Read the number of stones
    n = int(input())
    
    # Read the string representing the colors of the stones
    s = input()
    
    removals = 0
    
    # Start checking from the second stone (index 1) to the end
    for i in range(1, n):
        # If this stone is the same color as the previous one, we must remove it
        if s[i] == s[i - 1]:
            removals += 1
            
    # Print the total number of stones removed
    print(removals)

if __name__ == '__main__':
    solve()