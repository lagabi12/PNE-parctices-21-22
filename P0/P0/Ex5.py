import Seq0

list_genes = ["U5", "FRAT1", "ADA", "FXN", "RNU"]
FOLDER = "./sequences/"
for f in list_genes:
    seq = Seq0.seq_read_fasta(FOLDER + f)
    d = Seq0.seq_count(seq)
    print("GEN", f, d)