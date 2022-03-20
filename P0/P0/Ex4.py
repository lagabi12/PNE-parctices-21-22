import Seq0

list_genes = ["U5", "FRAT1", "ADA", "FXN", "RNU"]
FOLDER = "./sequences/"
BASES = ["A", "C", "T", "G"]

for f in list_genes:
    seq = Seq0.seq_read_fasta(FOLDER + f)
    print("GEN", f)
    for base in BASES:
        print(base, ":", Seq0.seq_count_bases(seq, base))