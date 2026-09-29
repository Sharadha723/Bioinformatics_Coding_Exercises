import sys

if len(sys.argv) < 2:
    print("Enter fasta file")
    sys.exit(1)

fasta_file = sys.argv[1]

def parse_data(seq):
    final_seq = {}
    for data in seq.strip().split('>'):
        if not data:
            continue
        lines = data.splitlines()
        rosalind_id = lines[0]
        sequence = ''.join(lines[1:])
        final_seq[rosalind_id] = sequence
            
    return (final_seq)

def profile_and_consensus(seq):
    first_sequence = list(seq.values())[0]
    profile = {'A': [0] * len(first_sequence),
               'C': [0] * len(first_sequence),
               'G': [0] * len(first_sequence),
               'T': [0] * len(first_sequence) }
    for sequence in seq.values():
        for i, nucleotide in enumerate(sequence):
            profile[nucleotide][i] += 1
    
    consensus = []
    for i in range(len(first_sequence)):
        nucleotide_counts = {
            'A': profile['A'][i],
            'C': profile['C'][i],
            'G': profile['G'][i],
            'T': profile['T'][i]}
        
        max_nucleotide = max(nucleotide_counts, key = nucleotide_counts.get)
        consensus.append(max_nucleotide)

    return ''.join(consensus), profile

file = open(fasta_file, 'r')
fasta_content = file.read()
file.close()

seq = parse_data(fasta_content)
consensus,profile = profile_and_consensus(seq)
print(consensus)
for nt in "ACGT":
    print(nt + ": " +' '.join(map(str, profile[nt])))