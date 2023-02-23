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
        req = self.client().post('/binary-number-addition', headers=headers, json={"numOne":"111001", "numTwo":"111110"})
        data = json.loads(req.data)

        self.assertEqual(data['status_code'], 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['result'], "1110111")


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


    def test_400_3_binary_number_addition(self):
        headers = {
            'Content-Type': 'application/json'
        }
        req = self.client().post('/binary-number-addition', headers=headers, json={"numOne":"111200", "numTwo":"1110"})
        data = json.loads(req.data)

        self.assertEqual(data['status_code'], 400)
        self.assertEqual(data['message'], 'bad request')
        self.assertEqual(data['success'], False)

    # test for binary number substraction
    def test_binary_number_substraction(self):
        headers = {
            'Content-Type':'application/json'
        }

        req = self.client().post('/binary-number-substraction', headers=headers, json={"numOne":"0011", "numTwo":"1110"})
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

    
    def test_400_3_binary_number_substraction(self):
        headers = {
            'Content-Type':'application/json'
        }

        req = self.client().post('/binary-number-substraction', headers=headers, json={"numOne":"0011", "numTwo":"1110"})
        data = json.loads(req.data)

        self.assertEqual(data['success'], False)
        self.assertEqual(data['status_code'], 400)
        self.assertEqual(data['message'], 'bad request')


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

    
    def test_404_binary_number_multiplication(self):
        headers = {
            'Content-Type': 'application/json'
        }

        req = self.client().post('/binary-number-multiplication', headers=headers, json={"numOne":"001100", "numTwo":"450111"})
        data = json.loads(req.data)

        self.assertEqual(data['status_code'], 400)
        self.assertEqual(data['message'], "bad request")
        self.assertEqual(data['success'], False)

    
    def test_404_2_binary_number_multiplication(self):
        headers = {
            'Content-Type': 'application/json'
        }

        req = self.client().post('/binary-number-multiplication', headers=headers, json={"numOne":"001100", "numTwo":"10101010100101010101001011010101010010101010100101101010101001010101010010110101010100101010101001011010101010010101010100101101010101001010101010010110101010100101010101001011010101010010101010100101101010101001010101010010110101010100101010101001011010101010010101010100101"})
        data = json.loads(req.data)

        self.assertEqual(data['status_code'], 400)
        self.assertEqual(data['message'], "bad request")
        self.assertEqual(data['success'], False)

    def test_400_3_binary_number_multiplication(self):
        headers = {
            'Content-Type': 'application/json'
        }

        req = self.client().post('/binary-number-multiplication', headers=headers, json={"numOne":"10101010", "numTwo":"11001100"})
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
        self.assertEqual(data['result'], {"the_result_of_division":"10", "remainder":"100"})

    
    def test_404_binary_number_division(self):
        headers = {
            'Content-Type': 'application/json'
        }

        req = self.client().post('/binary-number-division', headers=headers, json={"numOne":"001100", "numTwo":"450111"})
        data = json.loads(req.data)

        self.assertEqual(data['status_code'], 400)
        self.assertEqual(data['message'], "bad request")
        self.assertEqual(data['success'], False)

    
    def test_404_2_binary_number_division(self):
        headers = {
            'Content-Type': 'application/json'
        }

        req = self.client().post('/binary-number-division', headers=headers, json={"numOne":"001100", "numTwo":"10101010100101010101001011010101010010101010100101101010101001010101010010110101010100101010101001011010101010010101010100101101010101001010101010010110101010100101010101001011010101010010101010100101101010101001010101010010110101010100101010101001011010101010010101010100101"})
        data = json.loads(req.data)

        self.assertEqual(data['status_code'], 400)
        self.assertEqual(data['message'], "bad request")
        self.assertEqual(data['success'], False)


    
if __name__ == "__main__":
    unittest.main()
