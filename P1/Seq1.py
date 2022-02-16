class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases="NULL"):

        # Initialize the sequence with the value
        # passed as argument when creating the object
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

    def len(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            lenght = 0
        else:
            lenght = len(self.strbases)
        return lenght

    def seq_count_base(self):
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