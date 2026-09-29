import sys

if len(sys.argv) < 2:
    print("Enter protein seq file")
    sys.exit(1)

aa_seq_file = sys.argv[1]

file = open(aa_seq_file)
aa_seq = file.read().strip()
file.close()

codon_table = {'F': 2, 'L': 6, 'S': 6, 'Y': 2, 'C': 2, 'W': 1,'P': 4, 'H': 2, 'Q': 2, 'R': 6, 'I': 3, 'M': 1,'T': 4, 'N': 2, 'K': 2, 'V': 4, 'A': 4, 'D': 2,'E': 2, 'G': 4, 'STOP': 3}

def calc_no_rna_strings(seq):
    result = 1 #multiplying by 1 does not affect the result
    modulo = 1000000

    for aa in seq:
        result *= codon_table[aa]   #multiplying possibilities for each amino acid in given seq
        result %= modulo  #taking modulo at each step to avoid exceeding 1000000
    
    result *= codon_table['STOP']
    result %= modulo

    return result

result = calc_no_rna_strings(aa_seq)
print(result)

