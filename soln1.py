import operator

class soln:
    def __init__(self):
        self.numBooks = None
        self.numLib = None
        self.numDays = None
        self.scores = []
        self.libs = []

        self.libSorted = dict()
        self.libSorted2 = []

        self.usedBooks = set()

        self.librariesUsed = []

        self.booksUsed = []

    def importFile(self, filename):

        f = open(filename, "r")

        line = f.readline()
        self.numBooks = line.split()[0]
        self.numLib = line.split()[1] 
        self.numDays = line.split()[2] 
        line = f.readline()
        
        for i in line.split():
            self.scores.append(int(i))
            
        counter = 0
        books = 0
        while True:
            line = f.readline()
            if line == "" or line is None:
                break
            try:
                if counter % 2 == 0:
                
                    self.libs.append(Library(line.split()[0], line.split()[1], line.split()[2], books))
            
                else:

                    self.libs[books].addBooks(line.split())
                    self.libs[books].calcScore(self.scores)
                    books += 1
                

                counter += 1
            except:
                print("An exception occurred")
            
        f.close()

        #print(self.numBooks, self.numLib, self.numDays)
        #print(self.scores)
        #for i in self.libs:
           # print(i.numBooks, i.signup, i.ship, i.whichBooks, i.totalScore, i.number)


    
    def sortByScore(self):

        for library in self.libs:

            self.libSorted[library.number] = library.totalScore

        
        self.libSorted2 = sorted(self.libSorted.items(), key=operator.itemgetter(1))
    
    
    def countMin(self):
        
        daysUsed = 0
        daysLeft = int(self.numDays)
        check = True

        while True:

            for index, i in enumerate(self.libSorted2):

                daysUsed += self.incrementD(self.libs[index].signup, self.libs[index].whichBooks, self.libs[index].ship)

                daysLeft -= daysUsed
                
                if daysLeft <= 0:
                    check = False
                    break

                self.librariesUsed.append(index)

            if check == False:
                break
                
        
        f = open("cout.txt", "w")
        f.write(str(len(self.librariesUsed)) + "\n")

        for lib in self.librariesUsed:

            f.write(str(lib) + " " +str(len(self.libs[lib].whichBooks)) + "\n")

            f.write(str(self.libs[lib].whichBooks).strip("[],").replace(',', ' ') + "\n")
        
        f.close()

            
            
    def incrementD(self, signUp, libBooks, eachBooks):

        daysUsed = 0 

        daysUsed += int(signUp)
        bookCount = 0

        for book in libBooks:

            bookCount += int(eachBooks)
        
        

        return (int(daysUsed) + int(len(libBooks) / bookCount))



class Library:

    def __init__(self, books, signup, ship, number):

        self.numBooks = books
        self.signup = signup
        self.ship = ship
        self.whichBooks = []
        self.number = number
        self.totalScore = 0
    
    def addBooks(self, stringbooks):

        for i in stringbooks:
            self.whichBooks.append(int(i))

    
    def calcScore(self, scores):
        
        for i in self.whichBooks:
            self.totalScore += scores[i]



def main():

    s1 = soln()
    s1.importFile("c_incunabula.txt")
    s1.sortByScore()

    #for i in s1.libSorted:
        #print(i, s1.libSorted[i])

    #for i in s1.libSorted2:
       # print(i)

    s1.countMin()


if __name__ == "__main__":
    main()