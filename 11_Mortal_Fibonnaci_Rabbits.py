import sys

if len(sys.argv) < 3:
    print ("Enter n,m for mortal rabbit pairs")
    sys.exit(1)

n = int(sys.argv[1])
m = int(sys.argv[2])

if n > 100 or m > 20:
    print ("Enter appropriate values for n and m")
    sys.exit(1)

def mortal_fibonacci_rabbits(n,m):
    rabbits = [0]*m
    rabbits[0] = 1

    for month in range(1,n):
        new_rabbits = sum(rabbits[1:]) #only rabbits more than a month old will reproduce
        rabbits = [new_rabbits] + rabbits[:-1] #exclude aging/dead rbbits and shift to increase age
    return sum(rabbits)

result = mortal_fibonacci_rabbits(n,m)
print(result)
