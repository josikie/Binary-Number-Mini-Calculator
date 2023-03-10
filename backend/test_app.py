import unittest
from app import app
import json
import os
from urllib import request
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setDB, BinaryAddition, BinaryDivision, BinaryMultiplication, BinarySubstraction, setTestDB
from dotenv import load_dotenv
from app import create_app

DB_PATH = os.environ.get("DB_TEST_PATH")

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = DB_PATH

        with self.app.app_context():
            setTestDB(self.app, self.database_path)
            self.db = SQLAlchemy()
            self.db.init_app(self.app)


    def tearDown(self):
        pass

    
    # test for binary number addition
    def test_binary_number_addition(self):
        headers = {
            'Content-Type':'application/json'
        }
        req = self.client().post('/binary-number-addition', headers=headers, json={"numOne":"1110011", "numTwo":"101"})
        data = json.loads(req.data)

        self.assertEqual(data['status_code'], 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['result'], "1111000")


    def test_400_binary_number_addition(self):
        headers = {
            'Content-Type': 'application/json'
        }
        req = self.client().post('/binary-number-addition', headers=headers, json={"numOne":"111200", "numTwo":"1110"})
        data = json.loads(req.data)

        self.assertEqual(data['status_code'], 400)
        self.assertEqual(data['message'], 'bad request')
        self.assertEqual(data['success'], False)


    def test_400_2_binary_number_addition(self):
        headers = {
            'Content-Type': 'application/json'
        }
        req = self.client().post('/binary-number-addition', headers=headers, json={"numOne":"10101010100101010101001011010101010010101010100101101010101001010101010010110101010100101010101001011010101010010101010100101101010101001010101010010110101010100101010101001011010101010010101010100101101010101001010101010010110101010100101010101001011010101010010101010100101", "numTwo":"1110"})
        data = json.loads(req.data)

        self.assertEqual(data['status_code'], 400)
        self.assertEqual(data['message'], 'bad request')
        self.assertEqual(data['success'], False)


    # test for binary number substraction
    def test_binary_number_substraction(self):

        headers = {
            'Content-Type': 'application/json'
        }

        req = self.client().post('/binary-number-substraction', headers=headers,json={"numOne":"0011", "numTwo":"1110"})
        data = json.loads(req.data)

        self.assertEqual(data['result'], "-1011")
        self.assertTrue(data['success'])
        self.assertEqual(data['status_code'], 200)


    def tet_400_binary_number_substraction(self):
        headers = {
            'Content-Type': 'application/json'
        }

        req = self.client().post('/binary-number-substraction', headers=headers, json={"numOne":"111200", "numTwo":"1110"})
        data = json.loads(req.data)

        self.assertEqual(data['status_code'], 400)
        self.assertEqual(data['message'], 'bad request')
        self.assertEqual(data['success'], False)


    def test_400_2_binary_number_substraction(self):
        headers = {
            'Content-Type': 'application/json'
        }
        req = self.client().post('/binary-number-substraction', headers=headers, json={"numOne":"10101010100101010101001011010101010010101010100101101010101001010101010010110101010100101010101001011010101010010101010100101101010101001010101010010110101010100101010101001011010101010010101010100101101010101001010101010010110101010100101010101001011010101010010101010100101", "numTwo":"1110"})
        data = json.loads(req.data)

        self.assertEqual(data['status_code'], 400)
        self.assertEqual(data['message'], 'bad request')
        self.assertEqual(data['success'], False)


    # test for binary number multiplication
    def test_binary_number_multiplication(self):
        headers = {
            'Content-Type': 'application/json'
        }

        req = self.client().post('/binary-number-multiplication', headers=headers, json={"numOne":"1001010", "numTwo":"111100"})
        data = json.loads(req.data)

        self.assertTrue(data['success'])
        self.assertEqual(data['status_code'], 200)
        self.assertEqual(data['result'], "1000101011000")

    
    def test_400_binary_number_multiplication(self):
        headers = {
            'Content-Type': 'application/json'
        }

        req = self.client().post('/binary-number-multiplication', headers=headers, json={"numOne":"001100", "numTwo":"450111"})
        data = json.loads(req.data)

        self.assertEqual(data['status_code'], 400)
        self.assertEqual(data['message'], "bad request")
        self.assertEqual(data['success'], False)

    
    def test_400_2_binary_number_multiplication(self):
        headers = {
            'Content-Type': 'application/json'
        }

        req = self.client().post('/binary-number-multiplication', headers=headers, json={"numOne":"001100", "numTwo":"10101010100101010101001011010101010010101010100101101010101001010101010010110101010100101010101001011010101010010101010100101101010101001010101010010110101010100101010101001011010101010010101010100101101010101001010101010010110101010100101010101001011010101010010101010100101"})
        data = json.loads(req.data)

        self.assertEqual(data['status_code'], 400)
        self.assertEqual(data['message'], "bad request")
        self.assertEqual(data['success'], False)


    # test for binary number division
    def test_binary_number_division(self):
        headers = {
            'Content-Type': 'application/json'
        }

        req = self.client().post('/binary-number-division', headers=headers, json={"numOne":"111000", "numTwo":"11010"})
        data = json.loads(req.data)

        self.assertTrue(data['success'])
        self.assertEqual(data['status_code'], 200)
        self.assertEqual(data['result'], "10")
        self.assertEqual(data["remainder"], "100")

    
    def test_400_binary_number_division(self):
        headers = {
            'Content-Type': 'application/json'
        }

        req = self.client().post('/binary-number-division', headers=headers, json={"numOne":"00112", "numTwo":"00011"})
        data = json.loads(req.data)

        self.assertEqual(data['status_code'], 400)
        self.assertEqual(data['message'], "bad request")
        self.assertEqual(data['success'], False)

    
    def test_400_2_binary_number_division(self):
        headers = {
            'Content-Type': 'application/json'
        }

        req = self.client().post('/binary-number-division', headers=headers, json={"numOne":"001100", "numTwo":"10101010100101010101001011010101010010101010100101101010101001010101010010110101010100101010101001011010101010010101010100101101010101001010101010010110101010100101010101001011010101010010101010100101101010101001010101010010110101010100101010101001011010101010010101010100101"})
        data = json.loads(req.data)

        self.assertEqual(data['status_code'], 400)
        self.assertEqual(data['message'], "bad request")
        self.assertEqual(data['success'], False)

    
    # test for convert binary to decimal number
    def test_binary_to_decimal_number(self):
        headers = {
            'Content-Type': 'application/json'
        }

        req = self.client().get('/binary-to-decimal', headers=headers, json={"binaryNum":"01110110"})
        data = json.loads(req.data)

        self.assertEqual(data['status_code'], 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['result'], 118)

    
    def test_400_binary_to_decimal_number(self):
        headers = {
            'Content-Type': 'application/json'
        }

        req = self.client().get('/binary-to-decimal', headers=headers, json={"binaryNum":"-100711"})
        data = json.loads(req.data)

        self.assertEqual(data['status_code'], 400)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], "bad request")


    def test_400_binary_2_to_decimal_number(self):
        headers = {
            'Content-Type': 'application/json'
        }

        req = self.client().get('/binary-to-decimal', headers=headers, json={"binaryNum":"10101010100101010101001011010101010010101010100101101010101001010101010010110101010100101010101001011010101010010101010100101101010101001010101010010110101010100101010101001011010101010010101010100101101010101001010101010010110101010100101010101001011010101010010101010100101"})
        data = json.loads(req.data)

        self.assertEqual(data['status_code'], 400)
        self.assertEqual(data['message'], "bad request")
        self.assertEqual(data['success'], False)


    # test for convert decimal to binary endpoint
    def test_decimal_int_to_binary(self):
        headers = {
            'Content-Type': 'application/json'
        }  

        req = self.client().get('/decimal-to-binary', headers=headers, json={"decimalNum": 4095938384})
        data = json.loads(req.data)

        self.assertEqual(data['status_code'], 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['result'], "11110100001000110000111101010000")

    
    def test_negatif_decimal_int_to_binary(self):
        headers = {
            'Content-Type': 'application/json'
        }  

        req = self.client().get('/decimal-to-binary', headers=headers, json={"decimalNum": -4095938384})
        data = json.loads(req.data)

        self.assertEqual(data['status_code'], 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['result'], "-11110100001000110000111101010000")

    
    def test_decimal_float_to_binary(self):
        headers = {
            'Content-Type': 'application/json'
        }  

        req = self.client().get('/decimal-to-binary', headers=headers, json={"decimalNum": 40959.38384})
        data = json.loads(req.data)

        self.assertEqual(data['status_code'], 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['result'], "1001111111111111.01100010")

    
    def test_negatif_decimal_float_to_binary(self):
        headers = {
            'Content-Type': 'application/json'
        }  

        req = self.client().get('/decimal-to-binary', headers=headers, json={"decimalNum": -40959.38384})
        data = json.loads(req.data)

        self.assertEqual(data['status_code'], 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['result'], "-1001111111111111.01100010")


    # test for convert binary to decimal endpoint
    def test_binary_to_decimal(self):
        headers = {
            'Content-Type': 'application/json'
        }

        req = self.client().get('/binary-to-decimal', headers=headers, json={"binaryNum":"1100111"})
        data = json.loads(req.data)

        self.assertEqual(data['status_code'], 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['result'], 103)


    def test_negatif_binary_int_to_decimal(self):
        headers = {
            'Content-Type': 'application/json'
        }  

        req = self.client().get('/binary-to-decimal', headers=headers, json={"binaryNum":"-1100111"})
        data = json.loads(req.data)

        self.assertEqual(data['status_code'], 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['result'], -103)

    
    def test_decimal_float_to_binary(self):
        headers = {
            'Content-Type': 'application/json'
        }  

        req = self.client().get('/binary-to-decimal', headers=headers, json={"binaryNum": "1100111.110101"})
        data = json.loads(req.data)

        self.assertEqual(data['status_code'], 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['result'], 103.828125)

    
    def test_negatif_decimal_float_to_binary(self):
        headers = {
            'Content-Type': 'application/json'
        }  

        req = self.client().get('/binary-to-decimal', headers=headers, json={"binaryNum": "-1100111.110101"})
        data = json.loads(req.data)

        self.assertEqual(data['status_code'], 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['result'], -103.828125)


if __name__ == "__main__":
    unittest.main()
