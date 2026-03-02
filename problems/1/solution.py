import sys

if len(sys.argv) < 2:
    print("Please provide an argument for n")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("Argument must be an integer")
    sys.exit(1)

numbers = [i for i in list(range(1, n))]
multiples = [i for i in numbers if (i % 3 == 0) | (i % 5 == 0)]

print(f"Answer: {sum(multiples)}")