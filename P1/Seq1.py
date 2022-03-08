class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases="NULL"):

        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases
        if strbases == "NULL":
            print("NULL seq created")
            exit = False
        else:
            if not self.valid_sequence():
                self.strbases = "ERROR"
                print("INVALID seq!")
            else:
                print("New sequence created!")

    @staticmethod
    def valid_sequence2(sequence):
        valid = True
        i = 0
        while i < len(sequence):
            c = sequence[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid


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

    def len(self):
        """Calculate the length of the sequence"""
        if self.valid_sequence():
            return len(self.strbases)
        else:
            return 0


    def count_base(self):
        count_a = 0
        count_c = 0
        count_g = 0
        count_t = 0
        for i in self.strbases:
            if i == "A":
                count_a += 1
            elif i == "C":
                count_c += 1
            elif i == "G":
                count_g += 1
            elif i == "T":
                count_t += 1
        return count_a, count_c, count_g, count_t

    def count(self):
        d = {"A": 0, "C": 0, "G": 0, "T": 0}
        for b in self.strbases:
            try:
                d[b] += 1
            except BaseException:
                return d
        return d

    def reverse(self):
        if self.valid_sequence():
            fragment = self.strbases
            reverse = fragment[::-1]
            return reverse
        else:
            return self.strbases

    def complement(self):
        if self.valid_sequence():
            frag = self.strbases
            complementary = ""
            for i in frag:
                if i == "A":
                    complementary += "T"
                elif i == "T":
                    complementary += "A"
                elif i == "C":
                    complementary += "G"
                elif i == "G":
                    complementary += "C"
            return complementary
        else:
            return self.strbases

    def get_file(self):
        exit = False
        while not exit:
            folder = "./sequences/"
            self.filename = input("Enter the name of the file: ")
            try:
                filename = open(folder + self.filename + ".txt", "r")
                exit = True
                return filename
            except FileNotFoundError:
                if self.filename.lower() == "exit":
                    print("The program is finished. You pressed exit.")
                    filename = "none"
                    exit = True
                    return filename
                else:
                    print("File was not found")

    def read_fasta2(self, filename):
        from pathlib import Path
        file_contents = Path(filename).read_text()
        lines = file_contents.splitlines()
        body = lines[1:]
        self.strbases = ""
        for line in body:
            self.strbases += line

    def processing_genes(self, d):
        highest_value = 0
        for k, v in d.items():
            if int(v) > highest_value:
                highest_value = int(v)
                base = k
        return base