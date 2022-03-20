import Seq0

list_genes = ["U5", "FRAT1", "ADA", "FXN", "RNU"]
for l in list_genes:
    print("GEN", l, "---->", Seq0.seq_length(Seq0.seq_read_fasta("./sequences/" + l)))