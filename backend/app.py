from flask import Flask, abort, request, jsonify
from sqlalchemy import or_, and_
from binarynumber import (
    processBinaryAddition, 
    checkIfNotBinaryNumber,
    check_zero, 
    processBinarySubstraction, 
    processBinaryMultiplication, 
    processBinaryDivision)
from models import setDB, BinaryAddition, BinarySubstraction, BinaryMultiplication, BinaryDivision
from flask_cors import CORS


def create_app(test_config=None):
    app = Flask(__name__)
    setDB(app)
    CORS(app)


    def checkNumbers(binaryOne, binaryTwo, calculator):
        ## task: use filter_by, to check if there are numbers equal to binaryOne and binaryTwo.
        ## If none, it is okay to save it to db, otherwise just calculate it.
        if calculator == "+":
            binaryFromDb = BinaryAddition.query.filter(and_(BinaryAddition.first_binary_number==binaryOne, BinaryAddition.second_binary_number==binaryTwo)).all()
        elif calculator == "-":
            binaryFromDb = BinarySubstraction.query.filter(and_(BinarySubstraction.first_binary_number==binaryOne, BinarySubstraction.second_binary_number==binaryTwo)).all()
        elif calculator == "*":
            binaryFromDb = BinaryMultiplication.query.filter(and_(BinaryMultiplication.first_binary_number==binaryOne, BinaryMultiplication.second_binary_number==binaryTwo)).all()
        elif calculator == "/":
            binaryFromDb = BinaryDivision.query.filter(and_(BinaryDivision.first_binary_number==binaryOne, BinaryDivision.second_binary_number==binaryTwo)).all()
        return binaryFromDb


    @app.route('/binary-number-addition', methods=['POST'])
    def binaryNumberAddition():
        binaryNumber = request.get_json()
        binaryOne = binaryNumber.get('numOne')
        binaryTwo = binaryNumber.get('numTwo')

        findTheEqual = checkNumbers(binaryOne, binaryTwo, "+")        

        if len(binaryOne) > 255 or len(binaryTwo) > 255:
            abort(400)
        
        if checkIfNotBinaryNumber(binaryOne) and checkIfNotBinaryNumber(binaryTwo):
            abort(400)
        
        result = processBinaryAddition(binaryOne, binaryTwo)
        if len(findTheEqual) == 0:
            binaryAddition = BinaryAddition(binaryOne, binaryTwo, result)
            binaryAddition.insert()

        return jsonify({
            'status_code' : 200,
            'success' : True,
            'result' : result
        })


    @app.route('/binary-number-substraction', methods=['POST'])
    def binarySubstractions():
        binaryNumber = request.get_json()
        binaryOne = binaryNumber.get("numOne")
        binaryTwo = binaryNumber.get("numTwo")

        findTheEqual = checkNumbers(binaryOne, binaryTwo, "-")

        if len(binaryOne) > 255 or len(binaryTwo) > 255:
            abort(400)

        if checkIfNotBinaryNumber(binaryOne) and checkIfNotBinaryNumber(binaryTwo):
            abort(400)

        result = processBinarySubstraction(binaryOne, binaryTwo)
        if len(findTheEqual) == 0:
            binaryMultiplication = BinarySubstraction(binaryOne, binaryTwo, result)
            binaryMultiplication.insert()

        return jsonify({
            'result': result,
            'success': True,
            'status_code': 200
        })

    @app.route('/binary-number-multiplication', methods=['POST'])
    def binaryNumberMultiplication():
        binaryNumber = request.get_json()
        binaryOne = binaryNumber.get("numOne")
        binaryTwo = binaryNumber.get("numTwo")

        findTheEqual = checkNumbers(binaryOne, binaryTwo, "*")

        if len(binaryOne) > 255 or len(binaryTwo) > 255:
            abort(400)

        if checkIfNotBinaryNumber(binaryOne) and checkIfNotBinaryNumber(binaryTwo):
            abort(400)

        result = processBinaryMultiplication(binaryOne, binaryTwo)

        if len(findTheEqual) == 0:
            binaryMultiplication = BinaryMultiplication(binaryOne, binaryTwo, result)
            binaryMultiplication.insert()

        return jsonify({
            'status_code': 200,
            'success': True,
            'result': result
        })


    @app.route('/binary-number-division', methods=['POST'])
    def binaryNumberDivision():
        binaryNumber = request.get_json()
        binaryOne = binaryNumber.get("numOne")
        binaryTwo = binaryNumber.get("numTwo")

        findTheEqual = checkNumbers(binaryOne, binaryTwo, "/")

        if len(binaryOne) > 255 or len(binaryTwo) > 255:
            abort(400)

        if checkIfNotBinaryNumber(binaryOne) and checkIfNotBinaryNumber(binaryTwo):
            abort(400)
        
        result = processBinaryDivision(binaryOne, binaryTwo)

        if len(findTheEqual) == 0:
            binaryDivision = BinaryDivision(binaryOne, binaryTwo, result[1], result[0])
            binaryDivision.insert()

        return jsonify({
            'status_code': 200,
            'success': True,
            'remainder': result[1],
            'result': result[0]
        })


    @app.route('/binary-to-decimal', methods=['GET'])
    def binaryToDecimal():
        binaryNumber = request.get_json()["binaryNum"]

        if len(binaryNumber) > 255:
            abort(400)

        if checkIfNotBinaryNumber()


    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'status_code': 400,
            'message': 'bad request',
            'success': False
        })

    return app

app = create_app()

if __name__=="__main__":
    app.run()