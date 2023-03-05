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
    dataTypeFloat = isinstance(decimalNum, float)
    dataTypeInt = isinstance(decimalNum, int)
    stringArrBinary = ""
    minus = False

    if decimalNum < 0:
        minus = True

    if dataTypeInt:
        decimalNumber = int(decimalNum)
        if decimalNumber < 0:
            minus = True
        arrBinary = []
        while decimalNumber != 0:
            arrBinary.insert(0,decimalNumber % 2)
            decimalNumber = int(decimalNumber / 2)
        
        for i in arrBinary:
            stringArrBinary += str(i)
        
        if stringArrBinary == "":
            stringArrBinary += "0"

        if minus:
            stringArrBinary = "-" + stringArrBinary

    if dataTypeFloat:
        numInFrontOfPoint = int(decimalNum)
        decimalNum = int(decimalNum * pow(2,8))
        frontOfPoint = []
        behindOfPoint = []

        if minus:
            while decimalNum < numInFrontOfPoint:
                remainder = decimalNum % 2
                if remainder == 0:
                    behindOfPoint.append('0')
                elif remainder == 1:
                    behindOfPoint.append('1')
                decimalNum = int(decimalNum/2)

            while decimalNum < 0:
                remainder = decimalNum % 2
                if remainder == 0:
                    frontOfPoint.append('0')
                elif remainder == 1:
                    frontOfPoint.append('1')
                decimalNum = int(decimalNum/2)
        else:
            while decimalNum > numInFrontOfPoint:
                remainder = decimalNum % 2
                if remainder == 0:
                    behindOfPoint.append('0')
                elif remainder == 1:
                    behindOfPoint.append('1')
                decimalNum = int(decimalNum/2)

            while decimalNum > 0:
                remainder = decimalNum % 2
                if remainder == 0:
                    frontOfPoint.append('0')
                elif remainder == 1:
                    frontOfPoint.append('1')
                decimalNum = int(decimalNum/2)

        frontReverse = []
        behindReverse = []
        [frontReverse.append(frontOfPoint[i]) for i in range(len(frontOfPoint)-1, -1, -1)]
        [behindReverse.append(behindOfPoint[j]) for j in range(len(behindOfPoint)-1, -1, -1)]

        for i in frontReverse:
            stringArrBinary = stringArrBinary + i
        
        stringArrBinary = stringArrBinary + "."

        for j in behindReverse:
            stringArrBinary = stringArrBinary + j

        if stringArrBinary == "":
            stringArrBinary += "0"

        if minus:
            stringArrBinary = "-" + stringArrBinary

    return stringArrBinary

# TOMORROW TASK: Added logic for binary without point on this logic
def convertBToD(binary):
    minus = False
    isFloat = False
    if binary[0] == "-":
        minus = True
    
    binaryNumberBeforePoint = ""
    binaryNumberAfterPoint = ""

    for i in binary:
        if i == '.':
            isFloat = True

    if isFloat:
        splittedNumber = binary.split(".")
        binaryNumberBeforePoint = splittedNumber[0]
        print(binaryNumberBeforePoint)
        binaryNumberAfterPoint = splittedNumber[1]
        print(binaryNumberAfterPoint)

    reverseBinaryNumberBeforePoint = []
    [reverseBinaryNumberBeforePoint.append(binaryNumberBeforePoint[i]) for i in range(len(binaryNumberBeforePoint)-1, -1, -1)]
    if reverseBinaryNumberBeforePoint[len(reverseBinaryNumberBeforePoint)-1] == '-':
        reverseBinaryNumberBeforePoint.pop(len(reverseBinaryNumberBeforePoint)-1)

    total = 0
    for j in range(len(reverseBinaryNumberBeforePoint)-1, -1, -1):
        print(reverseBinaryNumberBeforePoint[j])
        k = float(reverseBinaryNumberBeforePoint[j]) * pow(2,j)
        print(k)
        total = total + k
        print(total)
    for l in range(0, len(binaryNumberAfterPoint)):
        k = float(binaryNumberAfterPoint[l]) * pow(2,(-1 * (l + 1)))
        total = total + k
    
    if minus:
        total = -1 * total
    return total


def checkIfNotBinaryNumber(stringBinary):
    notBinaryNumber = False
    for i in range(0, len(stringBinary)):
        if stringBinary[i] != '1':
            if i == 0 and stringBinary[i] == '-':
                notBinaryNumber = False
            elif stringBinary[i] != '0':
                notBinaryNumber = True

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


# intToBinary = convertDecimalToBinary(350)
# trueOrFalse = intToBinary == "101011110"
# print(intToBinary)
# print(trueOrFalse)

# floatToBinary = convertDecimalToBinary(40959.38384)
# trueOrFalse = floatToBinary == "1001111111111111.01100010"
# print(floatToBinary)
# print(trueOrFalse)

binaryToDecimal = convertBToD("-1101.11011")
print(binaryToDecimal)