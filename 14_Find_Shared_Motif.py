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

def common_substring(substring, strings):
    for s in strings:
        if substring not in s:
            return False
    return True

def find_lcs(strings):
    shortest_lcs = min(strings, key=len)
    lcs = ""

    for i in range(len(shortest_lcs)):
        for j in range(i + 1, len(shortest_lcs) + 1):
            substring = shortest_lcs[i:j]
            if common_substring(substring, strings):
                if len(substring) > len(lcs):
                    lcs = substring

    return lcs

file = open(fasta_file, 'r')
fasta_content = file.read()
file.close()

sequences_dict = parse_data(fasta_content)
sequences = list(sequences_dict.values())
result = find_lcs(sequences)
print(result)
