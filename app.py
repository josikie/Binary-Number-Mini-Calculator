from flask import Flask, abort, request, jsonify
from binarynumber import (
    processBinaryAddition, 
    checkIfNotBinaryNumber, 
    processBinarySubstraction, 
    processBinaryMultiplication, 
    processBinaryDivision)


app = Flask(__name__)


@app.route('/binary-number-addition', methods=['POST'])
def binaryNumberAddition():
    binaryNumber = request.get_json()
    binaryOne = binaryNumber.get('numOne')
    binaryTwo = binaryNumber.get('numTwo')

    if len(binaryOne) > 255 or len(binaryTwo) > 255:
        abort(400)
    
    if checkIfNotBinaryNumber(binaryOne, binaryTwo):
        abort(400)
    
    result = processBinaryAddition(binaryOne, binaryTwo)

    return jsonify({
        'status_code' : 200,
        'success' : True,
        'result' : result
    })


@app.route('/binary-number-substraction', methods=['POST'])
def binaryNumberSubstraction():
    binaryNumber = request.get_json()
    binaryOne = binaryNumber.get('numOne')
    binaryTwo = binaryNumber.get('numTwo')

    if len(binaryOne) > 255 or len(binaryTwo) > 255:
        abort(400)

    if checkIfNotBinaryNumber(binaryOne, binaryTwo):
        abort(400)

    result = processBinarySubstraction(binaryOne, binaryTwo)

    return jsonify({
        'status_code': 200,
        'success': True,
        'result': result
    })


@app.route('/binary-number-multiplication', methods=['POST'])
def binaryNumberMultiplication():
    binaryNumber = request.get_json()
    binaryOne = binaryNumber.get("numOne")
    binaryTwo = binaryNumber.get("numTwo")

    if len(binaryOne) > 255 or len(binaryTwo) > 255:
        abort(400)

    if checkIfNotBinaryNumber(binaryOne, binaryTwo):
        abort(400)

    result = processBinaryMultiplication(binaryOne, binaryTwo)

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

    if len(binaryOne) > 255 or len(binaryTwo) > 255:
        abort(400)

    if checkIfNotBinaryNumber(binaryOne, binaryTwo):
        abort(400)
    
    result = processBinaryDivision(binaryOne, binaryTwo)

    return jsonify({
        'status_code': 200,
        'success': True,
        'result': {
            'the_result_of_division': result[0],
            'remainder': result[1]
        }
    })


@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        'status_code': 400,
        'message': 'bad request',
        'success': False
    })