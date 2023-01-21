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
        self.assertEqual(data['success'], True)
        self.assertEqual(data['result'], '10001')


    def test_400_binary_number_addition(self):
        headers = {
            'Content-Type':'application/json'
        }
        req = self.client().post('/binary-number-addition', headers=headers, json={"numOne":"0000000000000000001111111000000000001111", "numTwo":"1110"})
        data = json.loads(req.data)

        self.assertEqual(data['status_code'], 400)
        self.assertEqual(data['message'], 'bad request')
        self.assertEqual(data['success'], False)


    def test_400_not_binary_number(self):
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
