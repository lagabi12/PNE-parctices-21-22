import Seq0

list_genes = ["U5", "FRAT1", "ADA", "FXN", "RNU"]
for l in list_genes:
    print("GEN", l, "---->", (len(Seq0.seq_read_fasta("./sequences/" + l))))