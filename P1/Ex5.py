from Seq1 import Seq

#Null sequence
s1 = Seq()
#valid sequence
s2 = Seq("ACTGA")
#invalid sequence
s3 = Seq("Invalid sequence")

print("Sequence 1:", "(Length:", Seq.len(s1), ")", f'{s1}')
countA, countC, countG, countT = Seq.seq_count_base(s1)
print("A:", countA, "C:", countC, "G:", countG, "T:", countT)
print("Sequence 1:", "(Length:", Seq.len(s2), ")", f'{s2}')
countA, countC, countG, countT = Seq.seq_count_base(s2)
print("A:", countA, "C:", countC, "G:", countG, "T:", countT)
print("Sequence 1:", "(Length:", Seq.len(s3), ")", f'{s3}')
countA, countC, countG, countT = Seq.seq_count_base(s3)
print("A:", countA, "C:", countC, "G:", countG, "T:", countT)