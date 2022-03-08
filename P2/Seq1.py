class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases="NULL"):
        self.strbases = strbases
        if self.strbases == "NULL":
            print("Null Seq created")
        else:
            if not self.valid_sequence():
                self.strbases = "ERROR"
                print("ERROR!!")
            else:
                print("New sequence created!")


    def valid_sequence(self):
        valid = True
        i = 0
        while i < len(self.strbases):
            c = self.strbases[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def read_fasta(self, filename):
        seq = open(filename, "r").read()
        seq = seq[seq.find("\n"):].replace("\n", "")
        return seq

    def len(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            lenght = 0
        else:
            lenght = len(self.strbases)
        return lenght

    def count_base(self):

        countA = 0
        countC = 0
        countG = 0
        countT = 0

        for i in self.strbases:
            if i == "A":
                countA += 1
            elif i == "C":
                countC += 1
            elif i == "G":
                countG += 1
            elif i == "T":
                countT += 1
        return countA, countC, countG, countT

    def count(self):
        d = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        for i in d:
            if i == "A":
                d['A'] += 1
            elif i == "C":
                d['C'] += 1
            elif i == "G":
                d['G'] += 1
            elif i == "T":
                d['T'] += 1
        return d


    def seq_reverse(self):
        if self.strbases == "NULL":
            reverse_seq = "NULL"
        elif self.strbases == "ERROR":
            reverse_seq = "ERROR"
        else:
            reverse_seq = self.strbases[::-1]
        return reverse_seq

    def comp(self):
        complement_seq = ""
        if self.strbases == "NULL":
            complement_seq = "NULL"
        elif self.strbases == "ERROR":
            complement_seq = "ERROR"
        else:
            for i in self.strbases:
                if i == "A":
                    complement_seq += "T"
                elif i == "G":
                    complement_seq += "C"
                elif i == "C":
                    complement_seq += "G"
                elif i == "T":
                    complement_seq += "A"
        return complement_seq

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