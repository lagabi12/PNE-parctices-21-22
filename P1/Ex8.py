from Seq1 import Seq

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("DGTTRR")


print(f"\n  Sequence 1:  (Length: {s1.len()})  {s1}")
d = s1.count()
for k,v in d.items():
    print(k + ":", str(v), end=" ")
print("\nReverse:", s1.reverse())
print("Complementary:", s1.complement())

print(f"\n  Sequence 2:  (Length: {s2.len()})  {s2}")
d = s2.count()
for k,v in d.items():
    print(k + ":", str(v), end=" ")
print("\nReverse:", s2.reverse())
print("Complementary:", s2.complement())

print(f"\n  Sequence 3:  (Length: {s3.len()})  {s3}")
d = s3.count()
for k,v in d.items():
    print(k + ":", str(v), end=" ")
print("\nReverse:", s3.reverse())
print("Complementary:", s3.complement())