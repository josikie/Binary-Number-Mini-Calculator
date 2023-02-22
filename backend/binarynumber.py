def processBinaryAddition(stringOne, stringTwo):
    # convert string binary to decimal
    decimalOne = convertBinaryToDecimal(stringOne)
    decimalTwo = convertBinaryToDecimal(stringTwo)
    # add the decimal binary
    addedDecimal = decimalOne + decimalTwo
    # convert the result to binary 
    return convertDecimalToBinary(addedDecimal)


def processBinarySubstraction(stringOne, stringTwo):
    # convert string binary to decimal
    decimalOne = convertBinaryToDecimal(stringOne)
    decimalTwo = convertBinaryToDecimal(stringTwo)
    # substract them
    substractedDecimal = decimalOne - decimalTwo
    # convert the result to binary
    return convertDecimalToBinary(substractedDecimal)
    

def processBinaryMultiplication(stringOne, stringTwo):
    # convert string binary to decimal
    decimalOne = convertBinaryToDecimal(stringOne)
    decimalTwo = convertBinaryToDecimal(stringTwo)
    # multiplicate them
    multiplicatedDecimal = decimalOne * decimalTwo
    # convert the result of binary
    return convertDecimalToBinary(multiplicatedDecimal)


def processBinaryDivision(stringOne, stringTwo):
    # convert string binary to decimal 
    decimalOne = convertBinaryToDecimal(stringOne)
    decimalTwo = convertBinaryToDecimal(stringTwo)
    # divide them
    dividedDecimal = decimalOne / decimalTwo
    reminderOfDividedDecimal = decimalOne % decimalTwo
    return [convertDecimalToBinary(dividedDecimal), convertDecimalToBinary(reminderOfDividedDecimal)]


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
    
    if stringArrBinary == "":
        stringArrBinary += "0"

    if minus:
        stringArrBinary = "-" + stringArrBinary
    return stringArrBinary


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


# print("masukkan")
# sOne = input()
# print(convertDecimalToBinary(sOne))