from Seq1 import Seq

s1 = Seq()
s1.read_fasta2("../P0/P0/sequences/U5")

print(f"Sequence 1:  (Length: {s1.len()})  {s1}")
d = s1.count()
print("Bases:", d)
print("Rev:", s1.reverse())
print("Comp:", s1.complement(), "\n")
