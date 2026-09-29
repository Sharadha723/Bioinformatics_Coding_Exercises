import sys

if len(sys.argv) < 3:
    print("Enter alphabet and n")
    sys.exit(1)

alphabet = sorted(sys.argv[1:-1])
n = int(sys.argv[-1])

def generate_string(alphabet, n, current = ""):
    if len(current) == n:
        print (current)
        return
    
    for symbol in alphabet:
        generate_string(alphabet, n, current + symbol)

generate_string(alphabet,n)
