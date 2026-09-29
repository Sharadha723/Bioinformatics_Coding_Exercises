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

def translate(rna_seq):
    protein =[]
    for i in range(0, len(rna_seq), 3):
        codon = rna_seq[i:i+3]
        if len(codon) == 3:
            aa = codon_table.get(codon)
            if aa == 'Stop':
                return ''.join(protein)
            if aa:  # skip if None
                protein.append(aa)
        else:
            break
    return ''.join(protein)

def remove_introns(seq, introns):
    for intron in introns:
        seq = seq.replace(intron, "")
    return seq

def dna_to_rna(seq):
    return seq.replace('T', 'U')

parsed_seq = parse_data(dna_seq)
actual_seq = list(parsed_seq.values())[0]
introns = list(parsed_seq.values())[1:]
exon_seq = remove_introns(actual_seq, introns)
rna_seq = dna_to_rna(exon_seq)
protein = translate(rna_seq)
print(protein)


