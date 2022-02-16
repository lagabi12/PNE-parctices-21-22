from Seq1 import Seq

#Null sequence
s1 = Seq()
#valid sequence
s2 = Seq("ACTGA")
#invalid sequence
s3 = Seq("Invalid sequence")

print("Sequence 1:", "(Length:", Seq.len(s1), ")", f'{s1}')
print("Sequence 1:", "(Length:", Seq.len(s2), ")", f'{s2}')
print("Sequence 1:", "(Length:", Seq.len(s3), ")", f'{s3}')