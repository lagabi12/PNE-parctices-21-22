import Seq0

seq = seq_read_fasta(filename)
sequence, reverse_seq, complement_seq = Seq0.seq_reverse(seq)
print("Gene 5:")
print("Frag:", sequence)
print("Rev:", reverse_seq)