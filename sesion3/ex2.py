def count_bases(seq):
    d = {"A": 0, "C": 0, "G": 0, "T":0}
    for b in seq:
        d[b] += 1
    return d
seq = input("Introduce the sequence: ")
print("Total lenght: ", len(seq))
for k, v in count_bases(seq).items():
    print(k + ":", v)