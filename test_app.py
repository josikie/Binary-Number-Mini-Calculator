import unittest
from app import app
import json

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client


    def tearDown(self):
        pass

    
    # test for binary number addition
    def test_binary_number_addition(self):
        headers = {
            'Content-Type':'application/json'
        }
        req = self.client().post('/binary-number-addition', headers=headers, json={"numOne":"0011", "numTwo":"1110"})
        data = json.loads(req.data)

        self.assertEqual(data['status_code'], 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['result'], "10001")


    def test_400_binary_number_addition(self):
        headers = {
            'Content-Type': 'application/json'
        }
        req = self.client().post('/binary-number-addition', headers=headers, json={"numOne":"111200", "numTwo":"1110"})
        data = json.loads(req.data)

        self.assertEqual(data['status_code'], 400)
        self.assertEqual(data['message'], 'bad request')
        self.assertEqual(data['success'], False)

    def test_400_binary_number_addition(self):
        headers = {
            'Content-Type': 'application/json'
        }
        req = self.client().post('/binary-number-addition', headers=headers, json={"numOne":"1110011000000000000000000000000011111000100", "numTwo":"1110"})
        data = json.loads(req.data)

        self.assertEqual(data['status_code'], 400)
        self.assertEqual(data['message'], 'bad request')
        self.assertEqual(data['success'], False)


    # test for binary number substraction
    def test_binary_number_substraction(self):
        headers = {
            'Content-Type':'application/json'
        }

        req = self.Client().post('/binary-number-substraction', headers=headers, json={"numOne":"0011", "numTwo":"1110"})
        data = json.loads(req.data)

        self.assertTrue(data['success'])
        self.assertEqual(data['status_code'], 200)
        self.assertEqual(data['result'], "")

    
    def tet_404_binary_number_substraction(self):
        headers = {
            'Content-Type': 'application/json'
        }

        req = self.client().post('/binary-number-addition', headers=headers, json={"numOne":"111200", "numTwo":"1110"})
        data = json.loads(req.data)

        self.assertEqual(data['status_code'], 400)
        self.assertEqual(data['message'], 'bad request')
        self.assertEqual(data['success'], False)


if __name__ == "__main__":
    unittest.main()
