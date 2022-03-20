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
    from pathlib import Path
    seq = Path(filename).read_text()
    seq = seq[seq.find("\n"):].replace("\n", "")
    return seq

def seq_length(seq):
    return len(seq)

def seq_count_bases(seq, base):
    seq = seq[seq.find("\n") + 1:]
    seq = seq.replace("\n", "")
    count = 0

    for e in seq:
        if e == base:
            count += 1
    return count

def seq_count(seq):
    d = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for i in seq:
        for b in d:
            if i == b:
                d[b] += 1
    return d

def seq_reverse(seq):
    sequence = seq[:20]
    reverse_seq = sequence[::-1]
    return sequence, reverse_seq

def seq_complement(seq):
    sequence = seq[:20]
    COMPLEMENTS = {"A": "T", "T": "A", "C": "G", "G": "C"}
    complement = ""
    for i in sequence:
        for c in COMPLEMENTS:
            if i == c:
                complement += COMPLEMENTS[c]
    return complement

def frequent_base(seq):
    most_common = ""
    count = seq_count(seq)
    for b in count:
        if most_common == "":
            most_common = b
        elif int(count[b]) > count[most_common]:
            most_common = b

    return most_common




