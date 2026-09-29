import sys

if len(sys.argv) < 2:
    print("Enter number")
    sys.exit(1)

n = int(sys.argv[1])
k = int(sys.argv[2])

def partial_permutations(n, k):
    modulo = 1000000
    result = 1
    for i in range(n, n-k, -1):
        result = (result *i) % modulo
    return result

print(partial_permutations(n,k))