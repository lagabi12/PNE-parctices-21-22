from Seq1 import Seq

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("DGTTRR")

print(f"Sequence 1:  (Length: {s1.len()})  {s1}")
d = s1.count()
print("Bases:", d)
print("Rev:", s1.reverse())

print(f" Sequence 2:  (Length: {s2.len()})  {s2}")
d = s2.count()
print("Bases:", d)
print("Rev:", s2.reverse())

print(f"Sequence 3:  (Length: {s3.len()})  {s3}")
d = s3.count()
print("Bases:", d)
print("Rev:", s3.reverse())