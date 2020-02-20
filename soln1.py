import numpy as np

class soln:
    def __init__(self):
        self.imortant1 = None
        self.important2 = None





    def importFile(self, filename):

        f = open(filename, "r")

        self.important1 = filename.split()[0]
        f.close()




    def writeOut(self, filename):

        f = open(filename, "w")
        f.write("Now the file has more content!")
        f.close()


def main():

    s1 = soln()
    s1.writeOut("out.txt")


if __name__ == "__main__":
    main()