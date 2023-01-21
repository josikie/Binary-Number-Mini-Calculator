from flask import Flask, abort


app = Flask(__name__)


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
    for i in range(0, deviation):
        sB = '0' + sB
    
    return sB


def addBinaryNumbers(stringOne, stringTwo):
    # take the length
    sOneLength = len(stringOne)
    sTwoLength = len(stringTwo)
    # check if the digits only 0 and 1.
    if checkIfNotBinaryNumber(stringOne, stringTwo):
        # abort(400)
        return "Please add only binary digits"
    # check if the digits less than 18
    if sOneLength > 255 or sTwoLength > 255:
        # abort(400)
        return "Please only add binary digits with length less than 255"
    # add 0 in front of string One, if stringTwo's size greater than stringOne.
    if sOneLength > sTwoLength:
        stringTwo = lengthLongerThan(sOneLength, sTwoLength, stringOne, stringTwo)
    # add 0 in front of string Two, if stringOne's size greater than stringTwo.
    if sTwoLength > sOneLength:
        stringOne = lengthLongerThan(sTwoLength, sOneLength, stringTwo, stringOne)
    # add binary numbers.
    sOneSTwo = ""
    temp = '0'
    for i in range(sOneLength, -1):
        number = '0'
        if stringOne[i] == '1' and stringTwo[i] == '1':
            if temp == '1' and i == 0:
                number = '1'
                sOneSTwo += number
                number = '1'
                temp = '0'
            elif temp == '0' and i == 0:
                number = '0'
                sOneSTwo += number
                number = "1"
                temp = "0"
            elif temp == '1':
                number = '1'
                temp = '1'
            elif temp == '0':
                number = '0'
                temp = '1'
        elif stringOne == '1' and stringTwo[i] == '0':
            if temp == '1' and i == 0:
                number = '0'
                sOneSTwo += number
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
                
    return {
        'stringOne' : stringOne,
        'stringTwo' : stringTwo
    }

print('Masukkan dua string binary number: ')
stringOne = input()
stringTwo = input()
print(addBinaryNumbers(stringOne, stringTwo))