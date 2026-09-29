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

def rev_complement(seq):
    complement = {'A':'T', 'G':'C', 'C':'G', 'T':'A'}
    rev_comp = ''.join(complement.get(nt, '') for nt in reversed(seq))
    return rev_comp

def find_rev_palindrome(seq):
    palindromes = []
    for length in range (4,13):
        for i in range (len(seq) - length +1):
            substring = seq[i:i+length]
            rev_comp_seq = rev_complement(substring)
            if substring == rev_comp_seq:
                palindromes.append((i+1, length))
    return palindromes

parsed_seq = parse_data(dna_seq)

for id, sequence in parsed_seq.items():
    result = find_rev_palindrome(sequence)
    for position,length in result:
        print(position,length)