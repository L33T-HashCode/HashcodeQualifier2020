import sys


def getPoints(pointsList, element):
    return pointsList[element]


def getLibraryValue(library):
    timeModifier = 0.30
    totalVal = 0
    print(library)
    for book in library["booksList"]:
        totalVal += int(book)
    return totalVal * timeModifier

    
if __name__ == "__main__":
    inputFileList = sys.argv[1:]

    for fileName in inputFileList:
        with open(fileName, "r") as fileHandle:
            inputFileContents = fileHandle.read().split('\n')

            #Every single book!
            totalNumOfBooks = int(inputFileContents[0].split(' ')[0])
            totalNumOfLibs = int(inputFileContents[0].split(' ')[1])
            totalNumOfDays = int(inputFileContents[0].split(' ')[2])

            #Print them name of the file
            """
            print("#############################")
            print("Total Number Of Books: " + str(totalNumOfBooks))
            print("Total Number Of Libs: " + str(totalNumOfLibs))
            print("Total Number Of Days: " + str(totalNumOfDays))
            print("#############################")
            """

            #Get scores
            bookScoreList = list()
            for i in inputFileContents[1].split(' '):
                bookScoreList += [int(i)]

            libsList = list()
            #Gets Libraries
            for i, j in zip(inputFileContents[2::2], inputFileContents[3::2]):
                if len(i) != 0:
                    libNumOfBooks = int(i.split(' ')[0])
                    libNumOfDaysSignup = int(i.split(' ')[1])
                    libNumOfBooksCanShipped = int(i.split(' ')[2])

                    libListOfBooks = j.split(' ')
                    
                    libDict = {
                        "daysSignup": libNumOfDaysSignup,
                        "booksToBeShipped": libNumOfBooksCanShipped,
                        "booksList": libListOfBooks,
                        "scanned":False
                    }

                    libsList += [libDict]

            outPutList = list()

            daysLeft = totalNumOfDays
            for i in libsList:
                if totalNumOfDays < 10: break

                # for j in i.get("booksList"):
                #     print(getPoints(bookScoreList, j))

            with open(fileName[:fileName.find('.txt')] + '.out', "w") as outHandle:
                outHandle.write(str(len(outPutList)) + '\n')
                for i in outPutList:
                    pass

            minStartTime = []

            i = 0

            for library in libsList:
                if (i == 0):
                    minStartTime.append(library["daysSignup"])
                else:
                    minStartTime.append(minStartTime[i-1]+library["daysSignup"])
                i += 1

            libraryStarted = 0
            scanning = False

            sortedByVal = sorted(libsList, key=lambda x: getLibraryValue(x))
            # most valuable libraries in terms of value 
            print("\n\nSorted by val {}".format(sortedByVal))

            # when scanning, only allow 1 library to scan
            # for every tick in the system
            for x in range(totalNumOfBooks):
                if (minStartTime[libraryStarted] == x):
                    # start the library associated with this start time
                    scanning = True
                    libraryStarted += 1
                else:
                    beingScanned = True

                for library in libraryStarted:
                    if (library["scanned"] == True):
                        # pick the x books and 
                        # send the x books alloted
                        pass

            ## expiration date has passed
            print(minStartTime)