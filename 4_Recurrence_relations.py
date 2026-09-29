import sys

if len(sys.argv) < 3:
    print ("Enter n,k for rabbit pairs")
    sys.exit(1)

n = int(sys.argv[1])
k = int(sys.argv[2])


if n > 40 or k > 5:
    print ("Enter appropriate values for n and k")
    sys.exit(1)

def rabbit_pairs(n,k):
    rabbits = [1,1]
    
    for month in range (2, n):
            rabbits.append(rabbits[-1] + k * rabbits[-2])
    return rabbits[-1]

result = rabbit_pairs(n,k)
print("The total number of rabbit pairs after",n, "months is",result)