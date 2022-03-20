import Seq0
filename = "./sequences/U5"
seq = Seq0.seq_read_fasta(filename)
sequence, reverse_seq = Seq0.seq_reverse(seq)
print("Gene 5:")
print("Frag:", sequence)
print("Rev:", reverse_seq)