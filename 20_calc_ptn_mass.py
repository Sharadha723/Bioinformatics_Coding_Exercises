import sys

if len(sys.argv) < 2:
    print("Enter protein seq file")
    sys.exit(1)

protein_file = sys.argv[1]

file = open(protein_file)
aa_seq = file.read().strip()
file.close()

aa_weights = {
    'A': 71.03711, 'C': 103.00919, 'D': 115.02694, 'E': 129.04259, 'F': 147.06841,
    'G': 57.02146, 'H': 137.05891, 'I': 113.08406, 'K': 128.09496, 'L': 113.08406,
    'M': 131.04049, 'N': 114.04293, 'P': 97.05276, 'Q': 128.05858, 'R': 156.10111,
    'S': 87.03203, 'T': 101.04768, 'V': 99.06841, 'W': 186.07931, 'Y': 163.06333,
}

def calc_weight_seq(seq):
    seq_weight = 0
    for s in seq:
        if s not in aa_weights:
            return ("Invalid amino acid entered")
        seq_weight += aa_weights[s]
    return seq_weight
    
result = calc_weight_seq(aa_seq)
print(round(result, 3))


