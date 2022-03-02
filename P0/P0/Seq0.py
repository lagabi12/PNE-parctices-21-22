def seq_ping():
    print("OK")

def valid_file():
    exit = False
    while not exit:
        filename = "./sequences/" + input("Name of file:")
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

def seq_count(seq):
    d = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for i in seq:
        if i == "A":
            d['A'] += 1
        elif i == "C":
            d['C'] += 1
        elif i == "G":
            d['G'] += 1
        elif i == "T":
            d['T'] += 1
    return d

def seq_reverse(seq):
    sequence = seq[:20]
    reverse_seq = sequence[::-1]
    complement_seq = ""
    for i in sequence:
        if i == "A":
            complement_seq += "T"
        elif i == "G":
            complement_seq += "C"
        elif i == "C":
            complement_seq += "G"
        elif i == "T":
            complement_seq += "A"
    return sequence, reverse_seq, complement_seq

def frequent_base(countA, countC, countG, countT):
    most_frequent = ""
    if countA > countC and countA > countG and countA > countT:
        most_frequent = "A"
    elif countC > countA and countC > countG and countC > countT:
        most_frequent = "C"
    elif countG > countA and countG > countC and countG > countT:
        most_frequent = "G"
    elif countT > countA and countT > countG and countT > countC:
        most_frequent = "T"

    return most_frequent




