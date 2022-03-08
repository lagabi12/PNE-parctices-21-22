from Seq1 import Seq

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("DGTTRR")

print(f"  Sequence 1:  (Length: {s1.len()})  {s1}")
a, c, g, t = s1.count_base()
print("A:", a, "C:", c, "T:", t, "G:", g)
print(f"  Sequence 2:  (Length: {s2.len()})  {s2}")
a, c, g, t = s2.count_base()
print("A:", a, "C:", c, "T:", t, "G:", g)
print(f"  Sequence 3:  (Length: {s3.len()})  {s3}")
a, c, g, t = s3.count_base()
print("A:", a, "C:", c, "T:", t, "G:", g)