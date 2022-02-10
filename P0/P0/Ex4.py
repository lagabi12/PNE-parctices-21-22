import Seq0

list_genes = ["U5", "FRAT1", "ADA", "FXN", "RNU"]
FOLDER = "./sequences/"
for f in list_genes:
    filename = FOLDER + f
    seq = Seq0.seq_read_fasta(filename)
    countA, countC, countG, countT = Seq0.seq_count_base(seq)
    print("GEN", f)
    print(" A:",countA, "\n", "C:", countC, "\n", "G:", countG, "\n", "T:", countT, "\n")