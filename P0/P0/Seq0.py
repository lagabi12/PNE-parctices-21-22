def seq_ping():
    print("OK")

def valid_file():
    exit = False
    while not exit:
        filename = input("Name of file:")
        try:
            f = open(filename)
            exit = True
            return filename
        except FileNotFoundError:
            print("File not found")

def seq_read_fasta(filename):
    seq = open(filename, "r").read()
    seq = seq[seq.find("\n"):].replace("\n", "")
    return seq

def seq_count_base(seq):
    countA = 0
    countC = 0
    countG = 0
    countT = 0

    for i in seq:
        if i == "A":
            countA += 1
        elif i == "C":
            countC += 1
        elif i == "G":
            countG += 1
        elif i == "T":
            countT += 1
    return countA, countC, countG, countT

