# Initial Fibonacci terms
f_n1 = 1
f_n2 = 1

# Starting conditions
n = 2
digits = 1

while digits < 1000:
    n += 1
    
    # Compute next Fibonacci number
    f_n = f_n1 + f_n2
    print(f"n: {n},   f_n: {f_n}")    

    # Update previous terms
    f_n2 = f_n1
    f_n1 = f_n

    # Update digit count
    digits = len(str(f_n))