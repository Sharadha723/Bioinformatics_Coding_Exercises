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

def adj_list(sequence, overlap_length=3):
    adjacency_list = []
    for id1, seq1 in sequence.items():
        suffix = seq1[-overlap_length:]
        for id2, seq2 in sequence.items():
            if id1 != id2 and seq2.startswith(suffix):
                adjacency_list.append((id1,id2))
    return adjacency_list

file = open(fasta_file, 'r')
fasta_content = file.read()
file.close()

sequences = parse_data(fasta_content)
adjacency_list = adj_list(sequences)
for edge in adjacency_list:
    print (edge[0], edge[1])