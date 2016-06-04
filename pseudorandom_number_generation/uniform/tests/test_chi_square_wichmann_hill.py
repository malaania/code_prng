from pseudorandom_number_generation.chi_square_test import *
from pseudorandom_number_generation.uniform.generators import *

seq =[ round(i,4) for i in wichmann_hill(1,1,1,10)]
seq.append(1.11)
seq.append(-1.32)
seq.append(3.22)
bins = make_bins_continuous((0.1,0.9),0.1,seq,1,1)

print(seq)
print(bins)