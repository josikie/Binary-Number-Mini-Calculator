def checkIfNotBinaryNumber(stringOne, stringTwo):
    notBinaryNumber = False
    for i in stringOne:
        if i != '1':
            if i != '0':
                notBinaryNumber = True

    for j in stringTwo:
        if j != '1':
            if j != '0':
                notBinaryNumber = True

    return notBinaryNumber


def lengthLongerThan(lenA, lenB, sA, sB):
    deviation = lenA - lenB
    charSB = []
    for i in sB:
        charSB.append(i)
    
    for i in range(0, deviation):
        charSB.insert(0, '0')
    
    stringSB = ""
    for i in charSB:
        stringSB += i
    
    return stringSB


def processBinaryAddition(stringOne, stringTwo):
    sOneSTwo = []
    temp = '0'
    for i in range(len(stringOne)-1, -1, -1):
        number = '0'
        if stringOne[i] == '1' and stringTwo[i] == '1':
            if temp == '1' and i == 0:
                number = '1'
                sOneSTwo.append(number)
                number = '1'
                temp = '0'
            elif temp == '0' and i == 0:
                number = '0'
                sOneSTwo.append(number)
                number = '1'
                temp = '0'
            elif temp == '1':
                number = '1'
                temp = '1'
            elif temp == '0':
                number = '0'
                temp = '1'
        elif stringOne[i] == '1' and stringTwo[i] == '0':
            if temp == '1' and i == 0:
                number = '0'
                sOneSTwo.append(number)
                number = '1'
                temp = '0'
            elif temp == '0' and i == 0:
                number = '1'
                temp = '0'
            elif temp == '1':
                number = '0'
                temp = '1'
            elif temp == '0':
                number = '1'
                temp = '0'
        elif stringOne[i] == '0' and stringTwo[i] == '1':
            if temp == '1' and i == 0:
                number = '0'
                sOneSTwo.append(number)
                number = '1'
                temp = '0'
            elif temp == '0' and i == 0:
                number = '1'
                temp = '0'
            elif temp == '1':
                number = '0'
                temp = '1'
            else:
                number = '1'
                temp = '0'
        elif stringOne[i] == '0' and stringTwo[i] == '0':
            if temp == '1':
                number = '1'
                temp = '0'
            elif temp == '0':
                number = '0'
                temp = '0'
        sOneSTwo.append(number)

    if sOneSTwo[len(sOneSTwo)-1] == '0':
        sOneSTwo.pop(len(sOneSTwo)-1)
        if sOneSTwo[len(sOneSTwo)-1] == '0':
            sOneSTwo.pop(len(sOneSTwo)-1)
    return sOneSTwo


def addBinaryNumbers(stringOne, stringTwo):
    # take the length
    sOneLength = len(stringOne)
    sTwoLength = len(stringTwo)
    result = ""
    
    # add 0 in front of string One, if stringTwo's size greater than stringOne.
    if sOneLength > sTwoLength:
        stringTwo = lengthLongerThan(sOneLength, sTwoLength, stringOne, stringTwo)

    # add 0 in front of string Two, if stringOne's size greater than stringTwo.
    if sTwoLength > sOneLength:
        stringOne = lengthLongerThan(sTwoLength, sOneLength, stringTwo, stringOne)

    # add binary numbers.
    reservedResult = processBinaryAddition(stringOne, stringTwo)
    ## reverse back to normal
    for i in range(len(reservedResult)-1, -1, -1):
        result = result + reservedResult[i]

    # return {
    #     'stringOne' : stringOne,
    #     'stringTwo' : stringTwo
    # }

    return result


def processBinarySubstraction(stringOne, stringTwo):
    lenOne = len(stringOne)
    lenTwo = len(stringTwo)
    

def substractBinaryNumber(stringOne, stringTwo):
    # take the length
    lenOne = len(stringOne)
    lenTwo = len(stringTwo)
    result = ""

    # add 0 in front of string one if stringOne's size greater than stringTwo.
    if lenOne > lenTwo:
        stringTwo = lengthLongerThan(lenOne, lenTwo, stringOne, stringTwo)
    # add 0 in front of string Two, if stringOne's size greater than stringTwo.
    if lenTwo > lenTwo:
        stringOne = lengthLongerThan(lenTwo, lenOne, stringTwo, stringOne)

    #substract binary numbers
    reservedResult = processBinarySubstraction(stringOne, stringTwo)


# convert binary number to decimal number
def convertBinaryToDecimal(binaryNum):
    minus = False
    charBinaryNum = []
    if binaryNum[0] == "-":
        minus = True
        for i in binaryNum:
            if i != "-":
                charBinaryNum.append(i)
        binaryNum = ""
        for i in charBinaryNum:
            binaryNum += i
        
    result = 0
    baseNum = 2
    listBinaryNum = []
    for i in binaryNum:
        listBinaryNum.append(int(i))
        
    listLength = len(listBinaryNum)
    listReverseDecimalNum = []
    for i in range(listLength-1, -1, -1):
        listReverseDecimalNum.append(listBinaryNum[i])
    total = 0
    for i in range(0, len(listReverseDecimalNum)):
        result = 0
        if listReverseDecimalNum[i] == 0:
            result = pow(baseNum, i) * 0
        else:
            result = pow(baseNum, i) * 1
        total = total + result
    
    if minus:
        total = total * -1
    return total

# convert decimal number to binary number
def convertDecimalToBinary(decimalNum):
    minus = False
    decimalNumber = int(decimalNum)
    if decimalNumber < 0:
        minus = True
    arrBinary = []
    while decimalNumber != 0:
        arrBinary.insert(0,decimalNumber % 2)
        decimalNumber = int(decimalNumber / 2)
    
    stringArrBinary = ""
    for i in arrBinary:
        stringArrBinary += str(i)
    
    if minus:
        stringArrBinary = "-" + stringArrBinary
    return stringArrBinary


print("masukkan")
sOne = input()
print(convertBinaryToDecimal(sOne))