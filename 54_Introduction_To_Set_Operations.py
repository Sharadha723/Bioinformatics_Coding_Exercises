import sys

if len(sys.argv) < 2:
    print("Enter file")
    sys.exit(1)

file = sys.argv[1]

open_file = open(file)
file = open_file.read()
open_file.close()

def parse_input(data):
    lines = data.strip().splitlines()
    n = int(lines[0])
    A = set(map(int, lines[1]. strip()[1:-1].split(',')))
    B = set(map(int, lines[2]. strip()[1:-1].split(',')))
    return n, A, B

def set_operations(n, A, B):
    universal = set(range(1, n+1))
    return [A.union(B), A.intersection(B), A.difference(B), B.difference(A), universal.difference(A), universal.difference(B)]

def format_set(s):
    return '{' + ', '.join(map(str, s)) + '}'

n,A,B = parse_input(file)
results = set_operations(n,A,B)

output_file = open("output.txt", "w")
for result in results:
    output_file.write(format_set(result) + "\n")
output_file.close()
