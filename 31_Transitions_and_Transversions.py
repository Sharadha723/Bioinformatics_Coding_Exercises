import sys

if len(sys.argv) < 2:
    print("Enter dna seq file")
    sys.exit(1)

dna_seq_file = sys.argv[1]

file = open(dna_seq_file)
dna_seq = file.read()
file.close()

def parse_data(seq):
    final_seq = {}
    for data in seq.strip().split('>'):
        if not data:
            continue
        lines = data.splitlines()
        rosalind_id = lines[0]
        sequence = ''.join(lines[1:])
        final_seq[rosalind_id] = sequence
            
    return final_seq

def transition_transversion_ratio(s1, s2):
    transitions = {('A', 'G'), ('G', 'A'), ('C', 'T'), ('T', 'C')}
    trans_count = 0
    tvs_count = 0

    for a, b in zip(s1, s2):
        if a != b:
            if (a, b) in transitions:
                trans_count += 1
            else:
                tvs_count += 1

    return trans_count/tvs_count if tvs_count !=0 else float('inf')

sequences = list(parse_data(dna_seq). values())
s1 = sequences[1]
s2 = sequences[0]

print(round(transition_transversion_ratio(s1, s2), 11))