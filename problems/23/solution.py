import math

def divisors(n):
    """
    Return all divisors of an integer using the square-root pairing property.
    Only values up to √n are checked. Whenever a divisor is found, its paired
    divisor (n // i) is also added. 
    """
    divs = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
    
    return sorted(divs)


def is_abundant(n):
    """Check whether a number is abundant using its set of divisors."""
    divs = divisors(n)
    if sum(divs) > 2 * n:
        return True
    else:
        return False


def find_abundants():
    """
    Identify all abundant numbers up to the problem's limit by testing each
    integer and adding those that satisfy the abundance condition.
    """
    abundants = set()
    for n in range(1, 28213 + 1):
        if is_abundant(n):
            abundants.add(n)
        else:
            continue
    
    return abundants


def find_non_abundant_sums(abundants):
    """
    Identify integers that cannot be written as sum of two abundant numbers. 
    All valid sums of abundant pairs up to the limit are generated, before 
    taking the complement of this set to give the desired outcome. 
    """
    abundants = sorted(abundants)
    abundant_sums = set()
    
    for i, a in enumerate(abundants):
        for b in abundants[i:]:
            s = a + b
            if s > 28213:
                break
            abundant_sums.add(s)

    non_abund_sums = [n for n in range(1, 28213 + 1) if n not in abundant_sums]

    return non_abund_sums
            

def main():
    abundants = find_abundants()
    non_abund_sums = find_non_abundant_sums(abundants)

    print(f"Answer: {sum(non_abund_sums)}")
    

if __name__ == "__main__":
    main()