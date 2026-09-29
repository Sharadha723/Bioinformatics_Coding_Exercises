import sys

if len(sys.argv) < 6:
    print("Enter 6 non-negative integers")
    sys.exit(1)

int_1 = int(sys.argv[1])
int_2 = int(sys.argv[2])
int_3 = int(sys.argv[3])
int_4 = int(sys.argv[4])
int_5 = int(sys.argv[5])
int_6 = int(sys.argv[6])

couples = [int_1, int_2, int_3, int_4, int_5, int_6]

def dom_offspring(couples):
    prob = [1,1,1,0.75,0.5,0]
    exp_offspring = sum(2*couples[i] * prob[i] for i in range(6))
    return exp_offspring

result = dom_offspring(couples)
print(result)