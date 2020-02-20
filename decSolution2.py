import sys
import time

OUT_DIR = "declanOut/" 

if __name__ == "__main__":
    inputFileList = sys.argv[1:]

    for fileName in inputFileList:
        with open(fileName, "r") as fileHandle:
            inputFileContents = fileHandle.read().split('\n')

            totalNumOfBooks = int(inputFileContents[0].split(' ')[0])
            totalNumOfLibs = int(inputFileContents[0].split(' ')[1])
            totalNumOfDays = int(inputFileContents[0].split(' ')[2])

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

                    f = 0
                    libListOfBooks = list()
                    for p in j.split(' '):
                        if f > libNumOfBooks: break

                        if p not in libListOfBooks:
                            libListOfBooks += [int(p)]
                        f += 1
                    
                    libDict = {
                        "daysSignup": libNumOfDaysSignup,
                        "booksToBeShipped": libNumOfBooksCanShipped,
                        "booksList": libListOfBooks
                    }

                    libsList += [libDict]

            outPutList = list()
            daysLeft = totalNumOfDays

            k = 0
            for i in libsList:
                #absolut rubbish
                libScores = list()
                if daysLeft < 36: break
                if i.get("daysSignup") > 35: continue

                daysLeft -= i.get('daysSignup')

                for j in i.get("booksList"):
                    libScores += [bookScoreList[int(j)]]
                
                outPutList += [{
                    "libNum": k,
                    "booksList": i.get('booksList')
                }]

                k += 1

            print(str(daysLeft) + ' ' + str(totalNumOfDays))
            with open(OUT_DIR + fileName[:fileName.find('.txt')] + '.out', "w") as outHandle:
                outHandle.write(str(len(outPutList)))
                for i in outPutList:
                    outHandle.write('\n')
                    outHandle.write(str(i.get('libNum')) + ' ' + str(len(i.get('booksList'))) + '\n')
                    
                    for j in i.get('booksList'):
                        outHandle.write(str(j) + ' ')
