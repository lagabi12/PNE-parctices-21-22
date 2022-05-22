class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases="NULL"):
        self.strbases = strbases
        if strbases == "NULL":
            self.strbases = "ERROR"
            print("NULL seq created")
        else:
            if not self.valid_sequence():
                print("INVALID seq!")
            else:
                print("New sequence created!")


    def valid_sequence(self):
        valid = True
        i = 0
        while i < len(self):
            c = self[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid

    def __str__(self):
        """Method called when the object is being printed"""
        return self.bases

    def len(self, valid):
        """Calculate the length of the sequence"""
        if valid:
            return len(self)
        else:
            return 0

    def count_base(self, base):
        seq = self[self.find("\n") + 1:]
        seq = seq.replace("\n", "")
        count = 0

        for e in seq:
            if e == base:
                count += 1
        percentage = round((count/len(seq))*100, 2)
        return count, percentage

    def count(self):
        d = {"A": 0, "C": 0, "G": 0, "T": 0}
        for i in self:
            for b in d:
                if i == b:
                   d[b] += 1
        return d

    def reverse(self, valid):
        if valid:
            fragment = self
            reverse = fragment[::-1]
            return reverse
        else:
            return self

    def complement(self, valid):
        if valid:
            sequence = self
            COMPLEMENTS = {"A": "T", "T": "A", "C": "G", "G": "C"}
            complement = ""
            for i in sequence:
               for c in COMPLEMENTS:
                   if i == c:
                        complement += COMPLEMENTS[c]
            return complement
        else:
            return "NONE"

    def read_fasta(self, file_name):
        from pathlib import Path

        file_cont = Path(file_name).read_text()
        lines = file_cont.splitlines()
        body = lines[1:]
        self.bases = ""
        for line in body:
            self.bases += line

    def frequent_base(self):
        most_common = ""
        seq = self
        c = self.count()
        for b in c:
            if most_common == "":
                most_common = b
            elif int(c[b]) > c[most_common]:
                most_common = b
        return most_common

    def sums(self, valid):
        n = 0
        NUM_BASES = {"A": 3, "T": -2, "C": 4, "G": -6}
        if valid:
            for i in self:
                for b in NUM_BASES:
                    if i == b:
                        n += NUM_BASES[b]
            return n
        else:
            return 0


