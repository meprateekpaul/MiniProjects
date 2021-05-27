# To Find the most frequent 2-mer of "GATCCAGATCCCCATAC". (You should solve this exercise by hand.)

seq = "CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA"
kmer3 = {}
i = 0
for i in range(len(seq)-3+1) :
    current = seq[i: i+3]
    print(current)

    if current in kmer3:
        count = kmer3.get(current)
        kmer3[current] = count + 1
    else:
        kmer3[current] = 1
       
print(kmer3)

#
#{'TAA': 1, 'AAA': 2, 'AAC': 2, 'ACG': 2, 'CGT': 3, 'GTG': 4, 'TGA': 2, 'GAG': 2, 'AGA': 2, 'GAA': 1, 'TGC': 1, 'GCT': 1, 'CTG': 1, 'GAT': 1, 'ATT': 1, 'TTA': 1, 'TAC': 1, 'ACA': 1, 'CAC': 1, 'ACT': 1, 'CTT': 1, 'TTG': 1, 'TGT': 2, 'GTT': 1, 'TTC': 1, 'TCG': 1, 'TGG': 1, 'GGT': 1, 'GTA': 1, 'TAT': 1}
#{'GA': 2, 'AT': 3, 'TC': 2, 'CC': 4, 'CA': 2, 'AG': 1, 'TA': 1, 'AC': 1}