from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restful import reqparse
from tinydb import TinyDB
import numpy as np
import os
import sys
from pydantic import BaseModel, ValidationError, field_validator, validator
from exceptions import ModelNotTrainedException
from typing import Dict, Union
from model import train_model, predict
from typing import List

import logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s %(message)s')


app = Flask(__name__)


CORS(app)

PAGE_SIZE = int(os.environ.get('PAGE_SIZE', 10))

if os.environ.get('FLASK_ENV') == 'test':
    db = TinyDB('test_db.json')
else:
    db = TinyDB('db.json')

class DBEntry(BaseModel):
    """A DB entry"""
    x: float
    y: float

@app.route('/add', methods=['POST'])
def add_route() -> Dict[str, str]:
    """Add a new entry to the database"""
    global db
    try:
        db_entry = DBEntry.model_validate_json(request.data)
    except ValidationError as e:
        return {'error': str(e)}

    db.insert(db_entry.model_dump())


    return {'status': 'ok'}


class ListRequest(BaseModel):
    """A request to list the database"""
    page: int = 1




@app.route('/list', methods=['GET'])
def list_route() -> Union[List[Dict[str, float]], Dict[str, str]]:
    """List the database"""
    global db

    try:
        list_request = ListRequest.model_validate(request.values.to_dict())
    except ValidationError as e:
        return {'error': str(e)}

    page = list_request.page

    examples = db.all()
    examples = examples[(page - 1) * PAGE_SIZE: page * PAGE_SIZE]
    return examples


from threading import Lock, Thread

test_loss_value = None

def train_model_thread():
    """Train the model in a separate thread and save the test loss to a file"""
    with app.app_context():
        global test_loss_value
        examples = db.all()
        if len(examples) > 0:

            x = np.array([example['x'] for example in examples])
            y = np.array([example['y'] for example in examples])
            test_loss_value = train_model(x, y)

            with open('test_loss.txt', 'w') as f:
                f.write(str(test_loss_value))

        training_lock.release()


training_lock = Lock()

@app.route('/train', methods=['GET'])
def train_route() -> Dict[str, str]:
    """Train the model"""
    if training_lock.locked():
        return {'status': 'Training in progress'}
    else:
        training_lock.acquire()
        thread = Thread(target=train_model_thread)
        thread.start()

        return {'status': 'ok'}
    

class PredictRequest(BaseModel):
    x: float

@app.route('/predict', methods=['POST'])
def predict_route() -> Dict[str, Union[float, str]]:
    """Predict the value of y for a given x with the trained model"""
    try:
        predict_request = PredictRequest.model_validate_json(request.data)
    except ValidationError as e:
        return {'error': str(e)}

    try:
        y = predict(predict_request.x)
        return {'y': float(y)}
    except ModelNotTrainedException as e:
        return {'error': str(e)}
    


if os.path.exists('test_loss.txt'):
    with open('test_loss.txt', 'r') as f:
        test_loss_value = float(f.read())


@app.route('/test_loss', methods=['GET'])
def test_loss_route() -> Dict[str, Union[float, str]]:
    """Get the test loss"""
    global test_loss_value
    if test_loss_value is not None:
        return {'loss': test_loss_value}
    else:
        return {'error': 'Training not done yet'}
        
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
