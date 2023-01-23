from flask import Flask, abort, request, jsonify
from binarynumber import addBinaryNumbers, checkIfNotBinaryNumber


app = Flask(__name__)


@app.route('/binary-number-addition', methods=['POST'])
def binaryNumberAddition():
    stringNumber = request.get_json()
    stringOne = stringNumber.get('numOne')
    stringTwo = stringNumber.get('numTwo')

    if stringOne > 20 or stringTwo > 20:
        abort(400)
    
    if checkIfNotBinaryNumber(stringOne, stringTwo):
        abort(400)
    
    result = addBinaryNumbers(stringOne, stringTwo)

    return jsonify({
        'status_code' : 200,
        'success' : True,
        'result' : result
    })


@app.route('/binary-number-substraction', methods=['POST']):
def binaryNumberSubstraction():
    stringNumber = request.get_json()
    stringOne = stringNumber.get('numOne')
    stringTwo = stringNumber.get('numTwo')

    if stringOne > 20 or stringTwo > 20:
        abort(400)

    if checkIfNotBinaryNumber(stringOne, stringTwo):
        abort(400)

    result = 


@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        'status_code': 400,
        'message': 'bad request',
        'success': False
    })