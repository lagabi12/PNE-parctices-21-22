from Seq1 import Seq

GENES = ("U5", "ADA", "FRAT1", "FXN", "RNU")
FOLDER = "../P0/P0/sequences/"
for gene in GENES:
    filename = FOLDER + gene
    s1 = Seq()
    s1.read_fasta2(filename)
    print("Sequence:", gene, "Most frequent base:", Seq.frequent_base(s1))