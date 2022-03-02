from Seq1 import Seq

list_genes = ["U5", "FRAT1", "ADA", "FXN", "RNU"]
FOLDER = "../P0/P0//sequences/"
for f in list_genes:
    filename = FOLDER + f
    s1 = Seq()
    seq = Seq.read_fasta(s1, filename)
    countA, countC, countG, countT = Seq.count_base(s1)
    most_frequent = Seq.frequent_base(countA, countC, countG, countT)

    print("Gene", f, ": Most frequent base:", most_frequent)