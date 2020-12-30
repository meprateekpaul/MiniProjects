#this python code converts any DNA sequence to its complementary DNA Seq
def Complement(sequence): 
    complementary = ""
    for char in sequence:
      if char=="A":
        complementary += "T"
      if char=="T":
        complementary += "A"
      if char=="G":
        complementary += "C"
      if char=="C":
        complementary += "G"
    return complementary

sequence1="TCACTCATCTCGCACATTTCCAGCGAGAATATTAAGCGTCTTTCCTTGAAGTAGAGGAGGAAGATCTTCCTCTACTGCAGCGGTAATTAAAACTTGTTCAGCATCTTCGATCAGCTCTGCTAAACGTGCACGACGACGAGCGTCAAGCTCAGCAAAAACATCATCAAGAATCAGAACAGGATCTTCCCCGAGGTCATGGCGAAGAAGATGATACGAAGCAAGTTTCAATGCGAGAGCAAAAGACCAAGTTTCTCCGTGCGAGGCATATCCTTTTGCCGGCATCTCCCCAAGAGAAAGCTCTATTTCATCTCGATGTGGCCCAAACAGAGTTATTCCTCGAGCGAACTCAGCTTGACGAGATCCCTGCAAGGAATCAAAAAGAGCTTGTTGTAAATCTTCTATATCAGGAGTCTCGTTAGAATTAATGAGAGAAGAAACTTTGAGAGAGCACTCCGGGTCAAGACTTGTTCGATACCTAGCATGCGCAAAAAAGTTTCCTGTCTTGTCTTCAGAAACTGAAGAATAAGCGTCCTTTAATCGGGGAGAGAGGTCATGAAGAAGCCTGAGGCGCGCATACATTAGTCGCCCACCTAACCCTGCAAGCTGATCATCCCAGATAGATAATGTTGACTCAAAATACGGATCTTTTGCGTAGCTATTTTTTTTGTCACCTCCACCAGGACTTAAAGCTTTCTTCAATAAAGCATTGCGCTGCTTCAAAGCTCGAGCGTAGTCTCCTTGAACTAACGCCCATTTAGGCTGCCGTGCAACAAGAAGCGCATCAAGAAAATCACGTCTTCCAGACGGGTCGCCTTTAATAAGTGATAGATCCTCTGGGGCAAATAAAACGGTCCTAATAATTCCCAGAATATCCCTGGGGCGCGACATTTGAGTCCTATTAATCCCCACTTTATTTGCGCGCCCAGGAATAATATCAACCTCGACAGTGGTACTGCGCCCTCTTCTACTAACAGCTGCCCTAATGACACTATGATCTGCACCGACTCGAACAAGTGGAGCATCACTAGCCACCCTATGTGACCGCAGAGTTGCGAGGTATCCGATAGCTTCGACTAGGTTTGTTTTACCTTGACCATTGGGGCCAACAAGAAATGTGACTCCTGGCTTGAGGGAAACATCTGTAGAGATGTAGTTTCGAAAGTCTGCAACCCATAGATGTGTGACGTGCAT"
print("sequence1:"+Complement(sequence1))
sequence2="TTAGTTAGTAAACCGCACTGGCATGAGAACATAGCGATACGAAGAGTCGCAGTCGCCATCTGCTTCTTTTTGACCACTGAGAACTGCTGGCTTACCAGGCTGGGTGAAAGCAAGTCTGGTAAAAGGAGACGAAACAGCGTTAAGTCCATCAATAAGGTAGGTCGGATTGAAGGCAATTTCGATGTCAGGACCAACTAACTGGCACTCAACCGCTTCGCTAGCCTGTGCATCCTCTCCCGTCCCCGCGTCGATGCTTACTTGTCCATCAACGAACCGAAGACGAACTGGCGTGTTTCGTTCTGCGACAATGGAGACGCGCTTGACAGCTTCGATAAGCACTTGAGTATCCACAATTGCTTCCGTATCGACACTGTTAGGGAAAATCGCTGAAACTTTGGGATAGTCACCATCGAGAAGGCGACTAGTTGTGCGACGTTGCCCTGCATCAAAGCCAATAAGGCCGTCACCTCCAGCTGCTTCCCCGAGGGCGACCGAAACCGAACCAGATGGCCCCAGAGATTTCGCTGTGTCGGAAAGCGTTCGAGCAGGAACAAGAACAACAGCGTTAATGTCCTCATCATCAGGACGCCAAGTCAGCTCACGCATGGCCAATCGATAACGGTCTGTAGCCAACAGTGTCATGCGTTCACCGTCGACCTCCATGCGAACACCCGTAAGAATGGGAAGCGTATCTGAACGATCAGCAGCAACGCTGACCTGGGCTACTGCATGCGTGAATACATCACCCGGAATGTGACCGCTCGGCTCAGGAGATACCGGGAGCGTGGGATATTCTTCCACGGGCATTTTTAGCAAGGAAAAACGACTGGATCCGCAAGCGACAGAAACTTTATTTCCGTCAGTAGTCACATCGACGGGTTTGCCTGGAAGTGTTTTTGAAATATCTGAAAGCATTCGTCCTAAAACTAATGCTCGGCCCGGTTCATGGACATCTGCCTCAACAGTTATACGTGCGGAAACTTCGTAATCGAACGCAGATAAAGTCAATGACCCGTCAGCGTCAGCTTCGAGAAGAATTCCGGCTAGAACCGGCGTAGGTGGACGATTAGGCAGGCCACGAGCTACCCAAGTGACTGCCTCAGTCAGCACGTCGCGCTCCACACGGAATCTCAC"
print("sequence2:"+Complement(sequence2))
sequence3="CTAAGTGGACTGTTGAGACCGTATGCGCGTGGTTAGTTCTGTTACCTGGTTATAGACAGAGCGTCGCTCCGCCATGAGCTGCCGGATCTTCTTGTCTGCATGCATGACAGTTGTGTGATCACGTCCACCGAACTGTTGGCCAATTTTGGGTAGGGAGAGCTCAGTCAGTTCACGGCATAGGTACATAGCAATCTGACGAGCATTGACGAGAGTGCGTGATCTAGAGGCGCTACACAGGTCGTCAATAGTGAGGTCAAAGTACCCAGCTGTTTGCGCCATGATTGTCGCAGCTGTGATCTGACTGATTTGCTGATCGGGCATGAGATCACGCAAAACAATTTCGGCGAGCCCTAGATCTACTTCTTGCCTATTTAAACTCGCGAAAGCAGTTACGCGTATGAGTGCTCCCTCTAGTTCACGAATATTGCTAGATATCCGACTCGCAATGAATTCAAGAACTTCGTCAGGAACTTTTAGTTGTTCCTGACGTGCTTTTTTCGAAAGAATTGCGATTCGTGTTTCTAAATCTGGCGGCTGGACGTCAGTAAGTAGACCCATTTCGAATCGAGACCGCATGCGTTCTTCGAAGCCAGAGAGCTGCTTTGGTGGAACATCAGAAGTAATGACTACTTGCTTATTGGCATTATGTAAAGTGTTAAAAGTGTGGAAAAATTCTTCCTGAGTCTGCATTTTTCCTGACAGGAACTGAATGTCATCAATAAGTAGAATGTCAGTTTCGCGATAGCGGCGTTGAAAGCTGCTAGCGCGATCATCGCGGATTGAGTTGATGAAATCATTTGTGAATTCTTCAGAGTTCACATATTTAACTCGAACCTTAGGATAGAGATTCTGCGCGTAGTGGCCTATCGCATGCAGTAGGTGTGTCTTGCCTAGGCCTGAATCACCATAGATGAAAAGCGGGTTGTAAGCTCGAGCGGGGGCCTCAGCGACAGCCACAGCGGCTGCATGGGCAAAACGGTTACTAGACCCAATCACGAATGTATCGAAGGTGTATTTAGGATTGAGGTGATCGCCACCTGAATCGTTTGTTGTTTGATTCTTGGTGCTACTTCCTGCTGGTTTACGTGGCCTGTCTGGTCCAGAATCATGATGAGCAGTTTCTGTGGAAACAGTATCTGCCACTCCCCCGAAGCGTTCTTGAGCAGCAGCAGAAGTTGCAGGAAGTGAATTTTCTCCGCTGGGCTTATTCGAGGGATGGTTATCTTCGATTTTCCAGCTGTCACTTTCGCTGTACATATCAAGAGTTGGCTGACTCGATTCCTCGATAGTTCCACGAATAGAGGAATCTACTGTTACCGCGAGGCGGATATCGCGACCAGTTTCCCGCGCTAGAGACTCCGTAAGAGACTCGCGAACGCGTGTCTCCACAATGTCTTTAGTGAATTCATCAGGTACGGCAATGATTGCGGTTGAGTCGAGAATTCCAACCAGCGCACATTGTGCGACGAAAGCTCGTTGCGGAGCAGGGATGCCTGCCTCCTGCAGAGAGTGCAGCGTCGCCGTCCAGATCCGGCTGGTGTCGCTTTGTTTTTCCGACAC"
print("sequence3:"+Complement(sequence3))
