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

def generate_signs(n):
    if n == 0:
        return [[]]
    smaller = generate_signs(n - 1)
    result = []
    for s in smaller:
        result.append(s + [1])
        result.append(s + [-1])
    return result

def signed_permutations(n):
    nums = list(range(1, n+1))
    all_perms = permutations(nums)
    all_signs = generate_signs(n)

    results = []
    for perm in all_perms:
        for sign in all_signs:
            signed = [a * b for a, b in zip(perm, sign)]
            results.append(signed)
    return results

result = signed_permutations(n)
print(len(result))
for r in result:
    print(' '.join(map(str, r)))