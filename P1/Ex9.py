from Seq1 import Seq

s1 = Seq()

filename = "../P0/P0/sequences/U5"
filename = Seq.read_fasta(filename)

d = Seq.count(filename)
print("Sequence 1:", "(Length:", Seq.len(filename), ")" f'{filename}')
print("Bases: ", d)
print("Rev: ", Seq.seq_reverse(filename))
print("Comp: ", Seq.comp(filename), "\n")