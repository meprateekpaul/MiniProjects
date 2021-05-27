#Code Challenge (2 points): Write a function PatternMatching that solves the Pattern Matching Problem. Then add PatternMatching to Replication.py.


def PatternMatching(Pattern, Genome):
    position = [ ]
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
           position.append(i)
    return position

Pattern = "ATAT"
Genome = "GATATATGCATATACTT"

print(PatternMatching(Pattern, Genome))

