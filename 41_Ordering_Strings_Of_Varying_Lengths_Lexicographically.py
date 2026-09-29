import sys

if len(sys.argv) < 3:
    print("Enter alphabet and n")
    sys.exit(1)

alphabet = sys.argv[1:-1]
n = int(sys.argv[-1])

def generate_string(alphabet, n, current = ""):
    if len(current) > 0:
        file.write(current + "\n")
    
    if len(current) == n:
        return
    
    for symbol in alphabet:
        generate_string(alphabet, n, current + symbol)

file = open("output.txt", "w")
generate_string(alphabet,n)
file.close()

