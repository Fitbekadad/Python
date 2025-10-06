import collections

Nucleotides = ["A", "C", "G", "T"]
DNA_reverseCOmplement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
        return tmpseq
