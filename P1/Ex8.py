from Seq1 import Seq

#Null sequence
s1 = Seq()
#valid sequence
s2 = Seq("ACTGA")
#invalid sequence
s3 = Seq("Invalid sequence")

list_genes = [s1, s2, s3]
for f in list_genes:
    d = Seq.count(f)
    if f == s1:
        print("Sequence 1:", "(Length:", Seq.len(f), ")" f'{f}')
    elif f == s2:
        print("Sequence 2:", "(Length:", Seq.len(f), ")" f'{f}')
    elif f == s3:
        print("Sequence 3:", "(Length:", Seq.len(f), ")" f'{f}')
    print("Bases: ", d)
    print("Rev: ", Seq.seq_reverse(f))
    print("Comp: ", Seq.comp(f), "\n")