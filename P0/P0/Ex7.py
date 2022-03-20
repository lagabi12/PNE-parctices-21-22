import Seq0
filename = "./sequences/U5"
seq = Seq0.seq_read_fasta(filename)
sequence, reverse_seq = Seq0.seq_reverse(seq)
complement = Seq0.seq_complement(seq)
print("Gene 5:")
print("Frag:", sequence)
print("Com:", complement)