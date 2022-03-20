from Seq1 import Seq
BASES = ["A", "C", "T", "G"]

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("DGTTRR")

print("Sequence 1: (Length:", s1.len(), ")", s1)
for base in BASES:
    print(base, ":", Seq.count_base(s1, base))
print("Sequence 2: (Length:", s2.len(), ")", s2)
for base in BASES:
    print(base, ":", Seq.count_base(s2, base))
print("Sequence 3: (Length:", s3.len(), ")", s3)
for base in BASES:
    print(base, ":", Seq.count_base(s3, base))