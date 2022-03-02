from Seq1 import Seq

s1 = Seq()

filename = "../P0/P0/sequences/U5"
filename = Seq.read_fasta(s1, filename)
d = Seq.count(s1)
print("Sequence 1:", "(Length:", Seq.len(s1), ")" f'{s1}')
print("Bases: ", d)
print("Rev: ", Seq.seq_reverse(s1))
print("Comp: ", Seq.comp(s1), "\n")