import sys

if len(sys.argv) < 2:
    print("Enter number")
    sys.exit(1)

n = int(sys.argv[1])

def factorial (n):
    result = 1
    for i in range (1, n+1):
        result *= i
    return result

def permutations(num):
    if len(num) == 1:
        return [[num[0]]]
    
    result = []
    for i in range(len(num)):
        current = num[i]
        remaining = num[:i] + num[i+1:]
        for p in permutations(remaining):
            result.append([current] + p)
    return result

numbers = list(range(1,n+1))

all_permutations = permutations(numbers)

print(factorial(n))

for p in all_permutations:
    print(' '.join(map(str, p)))