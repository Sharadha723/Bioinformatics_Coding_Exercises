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

def subsequence_indices(s, t):
    indices = []
    t_index = 0

    for i in range(len(s)):
        if t_index < len(t) and s[i] == t[t_index]:
            indices.append(i+1)
            t_index += 1
        if t_index == len(t):
            break
    return indices

sequences = list(parse_data(dna_seq). values())
if len(sequences[0]) >= len(sequences[1]):
    s = sequences[0]
    t = sequences[1]
else:
    s = sequences[1]
    t = sequences[0]

indices = subsequence_indices(s,t)
print(' '.join(map(str, indices)))
