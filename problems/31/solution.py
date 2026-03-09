TARGET = 200
COIN_VALUES = [1, 2, 5, 10, 20, 50, 100, 200]
ways = 0

def count_ways(i, remaining):
    """
    Count the ways to make a given target `remaining` value using coin values 
    from the ith position onwards.
    """
    global ways
    
    if i == len(COIN_VALUES) - 1:
        # Last coin must exactly fill the remainder
        if remaining % COIN_VALUES[i] == 0:
            ways += 1
        return
    
    # Fix coin and find max coin quantity without exceeding target value
    coin = COIN_VALUES[i]
    max_qty = remaining // coin
    
    # Iterate the different possible coin quantities we can take
    for qty in range(max_qty + 1):
        # Count the ways to make the new remaining target value using coin 
        # values from the (i+1)th position onwards
        count_ways(i + 1, remaining - qty * coin)

count_ways(0, TARGET)
print(f"Answer: {ways}")