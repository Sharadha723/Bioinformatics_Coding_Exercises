import sys

if len(sys.argv) < 3:
    print("Enter k, N values")
    sys.exit(1)

k = int(sys.argv[1])
N = int(sys.argv[2])

def factorial (n):
    result = 1
    for i in range (1, n+1):
        result *= i
    return result

def binomial_coefficient (n,k):
    return factorial(n) // (factorial(k) * factorial(n-k))

def calculate_probability(k, N):
    p = 1/4
    total_offspring = 2 ** k

    prob = 0
    for i in range (N, total_offspring +1):
        bin_coeff = binomial_coefficient(total_offspring, i)
        prob += bin_coeff * (p ** i) * ((1-p) ** (total_offspring - i))
    
    return prob

result = calculate_probability(k,N)
print (round(result, 3))