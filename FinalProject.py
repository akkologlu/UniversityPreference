class Student:  # I created student class.
    def __init__(self, sID, name, lastname):
        self.name = name
        self.lastname = lastname
        self.setID(sID)

    def getID(self):
        return self.__id

    def setID(self, sID):                       #  I did id private.
        if len(sID) == 6:
            self.__id = sID

    def __str__(self):
        return self.name + ' ' + self.lastname + ' ' + self.__id


def readFile() -> list:  # Here I transfered informations from 'student.txt' file to the records list.
    myFile = open('student.txt', 'r', encoding='utf-8')
    records = []
    for line in myFile:
        line = line.strip()
        records.append(line)
    myFile.close()
    return records


def fromListToObject(records):  # Here I made object records informations and added to stObjects list.
    stObjects = []
    for record in records:
        splitted = record.split()
        stObject = Student(splitted[0], splitted[1], splitted[-1])
        stObjects.append(stObject)
    return stObjects


studentRecords = readFile()
studentsList = fromListToObject(studentRecords)


def getidno(studentsList):  # This function is for searching student from it's id number.
    idno = input('Enter an id no..:')
    for stObject in studentsList:
        if stObject.getID() == idno:   #If the id in the class matches the id entered, it enters if.
            return stObject.name + ' ' + stObject.lastname
    return 'Student not found' #This message is given if it does not enter if.

#HERE I OPENED AND LISTED MY FILES.
uniFile = open('university.txt', 'r', encoding='utf-8')
uniList = []
for uniline in uniFile:
    uniline = uniline.strip()
    lines = uniline.split(',')
    uniList.append(lines)
uniFile.close()

ansFile = open('answers.txt', 'r', encoding='utf-8')
answerList = []
for anslines in ansFile:
    anslines = anslines.strip()
    answerList.append(anslines)
ansFile.close()

keyFile = open('key.txt', 'r', encoding='utf-8')
keyList = []
for keylines in keyFile:
    keylines = keylines.strip()
    keyList.append(keylines)
keyFile.close()


def maxPoint(uniList):
    max = int(uniList[0][2])  #I set the first score information on the university list to max.
    for points in uniList:
        if int(points[2]) >= int(max):
            max = int(points[2]) #If it finds a score greater than that then I changed the max.
    return max


def maxPointUniversity(uniList):  #Here I search for the max score I found earlier and match it to a university.
    maxPointList = []
    max = maxPoint(uniList)
    for points in uniList:
        if int(points[2]) == max:
            maxPointList.append(points)
    return maxPointList


def resulttxt():
    resulttext = open('result.txt', 'w', encoding='utf-8') #I open 'result.txt' with 'w'.
    for answer in answerList:
        splitted = answer.split(' ') #I separate the lines in my answer list from the spaces and call them splitted.
        if splitted[1] == 'B': #I check the type of book in the 1st index.
            trueCounter = 0 #I open counters for true false and blank answers.
            falseCounter = 0
            blankCounter = 0
            for i in range(len(splitted[2])): #I rotate the loop as many as the answer choices. And I describe the name i to each answer.
                if keyList[1][i] == splitted[2][i]: #I compare the 'keyList' with the answers.
                    trueCounter = trueCounter + 1

                elif splitted[2][i] == '*':
                    blankCounter = blankCounter + 1

                else:
                    falseCounter = falseCounter + 1

            for student in studentsList:
                if student.getID() == splitted[0]: #If the id in answer list is equal to the object id, I insert if.
                    unilers = []
                    for uniler in uniList: #Here I just put university names on a separate list.
                        unilers.append(uniler[1])
                    #And I write the informations to the file.
                    resulttext.write(str(student.getID()) + ',' + student.name + ',' + student.lastname + ',' + str(splitted[1]) + ',' + str(trueCounter) + ',' + str(falseCounter) + ',' + str(blankCounter) + ',' + str(trueCounter - (falseCounter / 4)) + ',' + str((trueCounter - (falseCounter / 4)) * 15) + ',' + unilers[int(splitted[3]) - 1] + ',' + unilers[int(splitted[4]) - 1] + '\n')

        #I do the same for the other booklet.
        elif splitted[1] == 'A':
            trueCounter = 0
            falseCounter = 0
            blankCounter = 0
            for i in range(len(splitted[2])):
                if keyList[0][i] == splitted[2][i]:
                    trueCounter = trueCounter + 1

                elif splitted[2][i] == '*':
                    blankCounter = blankCounter + 1

                else:
                    falseCounter = falseCounter + 1

            for student in studentsList:
                if student.getID() == splitted[0]:
                    unilers = []
                    for uniler in uniList:
                        unilers.append(uniler[1])
                    resulttext.write(str(student.getID()) + ',' + student.name + ',' + student.lastname + ',' + str(splitted[1]) + ',' + str(trueCounter) + ',' + str(falseCounter) + ',' + str(blankCounter) + ',' + str(trueCounter - (falseCounter / 4)) + ',' + str((trueCounter - (falseCounter / 4)) * 15) + ',' + unilers[int(splitted[3]) - 1] + ',' + unilers[int(splitted[4]) - 1] + '\n')


def sortStudents():
    resulttxt() #I call result function to reuse the result file.
    resultFile = open('result.txt', 'r', encoding='utf-8')
    pointResults = []
    for result in resultFile:
        result = result.strip()
        result = result.split(',')
        a = float(result[8]), result[2], result[3], result[1] #I put the necessary information in the result file into a list, taking the score first.
        pointResults.append(a)
        pointResults.sort()
        pointResults.reverse() #And I'm sorting the list.
    for i in pointResults:
        print(f"{i[0]} :{i[3]} {i[1]}") #Then I print in the format what I want.


settlers = []
unsettlers = []
def placement():
    resulttxt()
    resultList = []
    resultFile = open('result.txt', 'r', encoding='utf-8')
    for result in resultFile:
        result = result.strip()
        result = result.split(',')
        # I put the necessary information in the result file into a list, taking the score first.
        resultList.append(
            result[8] + ',' + result[0] + ',' + result[1] + ',' + result[2] + ',' + result[3] + ',' + result[4] + ',' +
            result[5] + ',' + result[6] + ',' + result[7])
    resultList.sort()
    resultList.reverse() #And I'm sorting the list.
    for result1 in resultList:
        result1 = result1.split(',')
        result1[1] = int(result1[1]) #I made the ID integer.
        result1[0] = float(result1[0]) #I made the point float.
        for answer in answerList:
            answer = answer.split(' ')
            if int(result1[1]) == int(answer[0]): #Checking that the ID in the result list and the id in the answer list match.
                if result1[0] >= float(uniList[int(answer[3]) - 1][2]) and int(uniList[int(answer[3]) - 1][3]) > 0: #Checking points and capaticy information
                    settlers.append(result1[2] + ' ' + result1[3] + ',' + uniList[int(answer[3]) - 1][1])
                    (uniList[int(answer[3]) - 1][3]) = int(uniList[int(answer[3]) - 1][3]) - 1 #Reduces capacity
                elif result1[0] >= float(uniList[int(answer[4]) - 1][2]) and int(uniList[int(answer[4]) - 1][3]) > 0: #The same processes are for the second choice.
                    (uniList[int(answer[4]) - 1][3]) = int(uniList[int(answer[4]) - 1][3]) - 1
                    settlers.append(result1[2] + ' ' + result1[3] + ',' + uniList[int(answer[4]) - 1][1])
                else: #Those who cannot make either of their two choices, fall here.
                    unsettlers.append(str(result1[1])+' '+result1[2] + ' ' + result1[3])


def departments():
    departments = []
    departments1 = []
    for element in uniList:
        a = element[1].find('sitesi') #I find the word 'sitesi' in the name index of universities.
        b = element[1][a + 7:] #And I'm showing after that word.
        departments.append(b) #And I'm putting them on a list.
    for department in departments:
        if department not in departments1: #The same departments enter more than once, I make it unique with 'not in'.
            departments1.append(department) #And I'm putting them to the new list.
    for department in departments1:
        print(department)


while True:
    print("""
        1-Get name from ID number
        2-Display universities with maximum points
        3-Create result.txt
        4-List the student information sorted by their score
        5-List the students placed in every university/department
        6-List the students who were not be able to placed anywhere
        7-List all the department
        q-Press q to exit
        """)

    operation = input('Enter the operation you want to do...:')
    if operation == str(1):
        st = getidno(studentsList)
        print(st)


    elif operation == str(2):
        maxPointUni = maxPointUniversity(uniList)
        for unis in maxPointUni:
            print(unis[1] + ' ' + unis[2])


    elif operation == str(3):
        resulttxt()
        print('result.txt has been created')


    elif operation == str(4):
        sortStudents()


    elif operation == str(5):
        placement()
        uninames = []
        for i in uniList:
            uninames.append([i[1]])
        for settler in settlers:
            settler = settler.split(',')
            for uniname in uninames:
                if uniname[0] == settler[1]:
                    uniname.append(settler[0])
        for i in uninames:
            print('*' * 60)
            for j in i:
                print(j)
        break


    elif operation == str(6):
        placement()
        print('****UNSETTLERS****')
        for unsettler in unsettlers:
            print(unsettler)
        break



    elif operation == str(7):
        departments()

    elif operation == 'q':
        break