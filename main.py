from DNAtoolkit import*
import random

randDNAStr = ''.join([random.choice(Nucleotides) for nuc in range(50)])


DNAStr = validateSeq(randDNAStr)

print(countNucFrequency(DNAStr))
