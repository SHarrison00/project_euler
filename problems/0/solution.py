import sys

if len(sys.argv) < 2:
    print("Please provide an argument for n")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("Argument must be an integer")
    sys.exit(1)

numbers = [i ** 2 for i in list(range(1, n + 1))]
odd_squares = [i for i in numbers if i % 2 != 0]

print(f"Answer: {sum(odd_squares)}")