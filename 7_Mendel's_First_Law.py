import sys

if len(sys.argv) < 4:
    print("Enter k,m,n")
    sys.exit(1)

k = int(sys.argv[1])
m = int(sys.argv[2])
n = int(sys.argv[3])

if k<0 or m<0 or n<0:
    print ("Enter positive integers")
    sys.exit(1)

def dom_allele_probability(k,m,n):
    total = k+m+n
   
    # probability of picking each pair
    prob_AA_AA = (k/total) * ((k-1) / (total -1))
    prob_AA_Aa = (k/total) * (m / (total-1)) * 2 #for both types of pairing - AA_Aa and Aa_AA
    prob_AA_aa = (k/total) * (n/(total-1)) * 2  # for both types of pairing - AA_aa and aa_AA     
    prob_Aa_Aa = (m/total) * ((m-1) / (total - 1))
    prob_Aa_aa = (m/total) * (n / (total-1)) * 2
    prob_aa_aa = (n/total) * ((n-1) / (total - 1))       

    # probability of getting dominant phenotype from each pair
    prob_dominant = ((prob_AA_AA * 1) + (prob_AA_Aa * 1) + (prob_AA_aa * 1) + (prob_Aa_Aa * 0.75) + (prob_Aa_aa * 0.50) + (prob_aa_aa * 0))   

    return round(prob_dominant, 5)

result = dom_allele_probability(k,m,n)
print ("Probability of dominant phenotype = ", result)