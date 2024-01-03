import unittest
from flask_app import app
import time
import math


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test01_predict_endpoint_before_train(self):
        response = self.app.post('/predict',  json={'x': 1.5})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['error'], 'Model not trained yet')

    def test02_predict_endpoint_invalid(self):
        response = self.app.post('/predict',  json={'x': "hello"})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('error' in response.json)


    def test03_loss_endpoint_before_train(self):
        response = self.app.get('/test_loss')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['error'], 'Training not done yet')

    def test04_list_endpoint(self):
        response = self.app.get('/list')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 0)

    def test05_add_endpoint(self):
        response = self.app.post('/add',  json={'x': 12, 'y': 34})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['status'], 'ok')



    def test06_list_after_add(self):
        response = self.app.get('/list')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 1)
        self.assertEqual(response.json[0]['x'], 12)
        self.assertEqual(response.json[0]['y'], 34)
    
    def test07_multiple_add(self):
        response = self.app.post('/add',  json={'x': 56, 'y': 78})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['status'], 'ok')
        response = self.app.post('/add',  json={'x': 90, 'y': 12})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['status'], 'ok')

    def test08_list_after_multiple_add(self):
        response = self.app.get('/list')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 3)
        self.assertEqual(response.json[0]['x'], 12)
        self.assertEqual(response.json[0]['y'], 34)
        self.assertEqual(response.json[1]['x'], 56)
        self.assertEqual(response.json[1]['y'], 78)
        self.assertEqual(response.json[2]['x'], 90)
        self.assertEqual(response.json[2]['y'], 12)
    
    def test09_fill_database(self):
        for i in range(100):
            response = self.app.post('/add',  json={'x': i, 'y': i*math.sin(i)})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['status'], 'ok')

    def test10_train_endpoint(self):
        response = self.app.get('/train')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['status'], 'ok')
        # Wait for training to finish
        time.sleep(2)

    def test11_predict_after_train(self):
        response = self.app.post('/predict',  json={'x': 99})
        self.assertEqual(response.status_code, 200)

    def test12_loss_after_train(self):
        response = self.app.get('/test_loss')
        self.assertEqual(response.status_code, 200)



if __name__ == '__main__':
    unittest.main()