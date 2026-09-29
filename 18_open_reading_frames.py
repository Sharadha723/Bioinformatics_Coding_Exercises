import sys

if len(sys.argv) < 2:
    print("Enter fasta file")
    sys.exit(1)

seq_file = sys.argv[1]

codon_table = {'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L',
               'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S',
               'UAU':'Y', 'UAC':'Y', 'UAA':'Stop', 'UAG':'Stop',
               'UGU':'C', 'UGC':'C', 'UGA':'Stop', 'UGG':'W',
               'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
               'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
               'CAU':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q',
               'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
               'AUU':'I', 'AUC':'I', 'AUA':'I', 'AUG':'M',
               'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
               'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K',
               'AGU':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
               'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
               'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
               'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
               'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'}

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

def translate(seq):
    aa_seq = ""
    for i in range(0, len(seq) - 2, 3):
        codon = seq[i:i+3]
        aa = codon_table.get(codon)
        if aa == 'Stop':
            return aa_seq
        if aa:  # skip if None
            aa_seq += aa
        else:
            break
    return ""


def dna_to_rna(seq):
    return seq.replace('T', 'U')

def rev_complement(seq):
    complement = {'A':'T', 'G':'C', 'C':'G', 'T':'A'}
    rev_comp = ''.join(complement.get(nt, '') for nt in reversed(seq))
    return rev_comp

def find_orf(seq):
    orfs = []
    for frame in range(3):
        i = frame
        while i < len(seq) - 2:
            codon = seq[i:i+3]
            if codon == 'AUG':
                protein = translate(seq[i:])
                if protein and protein not in orfs:
                    orfs.append(protein)
            i += 1
    return orfs


def find_ptn_from_orf(seq):
    rna = dna_to_rna(seq)
    reverse_rna = dna_to_rna(rev_complement(seq))
    proteins = set(find_orf(rna) + find_orf(reverse_rna))
    return proteins

file = open(seq_file)
fasta_file = file.read()
file.close()

dna_seq = parse_data(fasta_file)
for header, seq in dna_seq.items():
    results = find_ptn_from_orf(seq)
    for result in results:
        print(result)
