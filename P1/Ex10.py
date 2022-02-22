from Seq1 import Seq

list_genes = ["U5", "FRAT1", "ADA", "FXN", "RNU"]
FOLDER = "../P0/P0//sequences/"
for f in list_genes:
    filename = FOLDER + f
    seq = Seq.read_fasta(filename)
    countA, countC, countG, countT = Seq.count_base(seq)
    most_frequent = Seq.frequent_base(countA, countC, countG, countT)

    print("Gene", f, ": Most frequent base:", most_frequent)