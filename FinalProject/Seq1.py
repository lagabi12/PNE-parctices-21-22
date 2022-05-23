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
        while i < len(self.strbases):
            c = self.strbases[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid

    def __str__(self):
        """Method called when the object is being printed"""
        return self.bases


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

    def count_bases(self):
        d = {"A": 0, "C": 0, "G": 0, "T": 0}
        for b in self.strbases:
            d[b] += 1
        total = sum(d.values())
        for k, v in d.items():
            d[k] = [v, (v * 100) / total]
        return d

    def reverse(self, valid):
        if valid:
            fragment = self
            reverse = fragment[::-1]
            return reverse
        else:
            return self


    def read_fasta(self, file_name):
        from pathlib import Path

        file_cont = Path(file_name).read_text()
        lines = file_cont.splitlines()
        body = lines[1:]
        self.bases = ""
        for line in body:
            self.bases += line



