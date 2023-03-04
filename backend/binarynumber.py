def processBinaryAddition(stringOne, stringTwo):
    # convert string binary to decimal
    stringOne = check_zero(stringOne)
    stringTwo = check_zero(stringTwo)
    decimalOne = convertBinaryToDecimal(stringOne)
    decimalTwo = convertBinaryToDecimal(stringTwo)
    # add the decimal binary
    addedDecimal = decimalOne + decimalTwo
    # convert the result to binary 
    return convertDecimalToBinary(addedDecimal)


def processBinarySubstraction(stringOne, stringTwo):
    # convert string binary to decimal
    stringOne = check_zero(stringOne)
    print(stringOne)
    stringTwo = check_zero(stringTwo)
    print(stringTwo)
    decimalOne = convertBinaryToDecimal(stringOne)
    decimalTwo = convertBinaryToDecimal(stringTwo)
    # substract them
    substractedDecimal = decimalOne - decimalTwo
    # convert the result to binary
    return convertDecimalToBinary(substractedDecimal)
    

def processBinaryMultiplication(stringOne, stringTwo):
    # convert string binary to decimal
    stringOne = check_zero(stringOne)
    stringTwo = check_zero(stringTwo)
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
    if decimalNum < 0:
        minus = True
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


def checkIfNotBinaryNumber(stringBinary):
    notBinaryNumber = False
    for i in range(0, len(stringBinary)):
        if stringBinary[i] != '1':
            if i == 0 and stringBinary[i] == '-':
                notBinaryNumber = False
            elif stringBinary[i] != '0':
                notBinaryNumber = True
            
            

    # for j in stringTwo:
    #     if j != '1':
    #         if j != '0':
    #             notBinaryNumber = True

    return notBinaryNumber

def check_zero(strings):
    char_list = []
    for i in strings:
        char_list.append(i)
    
    for j in range(0, len(char_list)):
        if char_list[0] == '0':
            char_list.pop(0)

    newString = ""
    for k in char_list:
        newString += k
    
    return newString


processBinarySubstraction("0011", "1101")
# print("masukkan")
# sOne = "00010100"
# print(check_zero(sOne))