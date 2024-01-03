from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.callbacks import TensorBoard, ModelCheckpoint
from tensorflow.keras.models import load_model
import os
import numpy as np
from exceptions import ModelNotTrainedException
from typing import Tuple


current_model = None

tensorboard = TensorBoard(log_dir='./logs', histogram_freq=0, write_graph=True, write_images=False)



def create_model() -> Sequential:
    model = Sequential()
    model.add(Dense(1, input_dim=1, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(1, activation='linear'))
    model.compile(loss='mse', optimizer=SGD(lr=0.01, momentum=0.9, nesterov=True))
    return model




def train_test_split(x: np.ndarray, y: np.ndarray, test_size=0.2, random_state=None) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    if random_state is not None:
        np.random.seed(random_state)

    num_samples = x.shape[0]
    num_test_samples = int(test_size * num_samples)
    test_indices = np.random.choice(num_samples, size=num_test_samples, replace=False)
    mask_test = np.zeros(num_samples, dtype=bool)
    mask_test[test_indices] = True
    x_train, x_test = x[~mask_test], x[mask_test]
    y_train, y_test = y[~mask_test], y[mask_test]
    return x_train, x_test, y_train, y_test




def train_model(x: np.ndarray, y: np.ndarray) -> float:
    global current_model

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    if current_model is None:
        if os.path.exists('model.keras'):
            current_model = load_model('model.keras')
        else:
            current_model = create_model()

    current_model.fit(x_train, y_train, epochs=10, verbose=1, callbacks=[tensorboard])

    score = current_model.evaluate(x_test, y_test)

    current_model.save('model.keras')

    return score


def predict(x : float) -> float:
    global current_model

    if current_model is None:
        if os.path.exists('model.keras'):
            current_model = load_model('model.keras')
        else:
            raise ModelNotTrainedException('Model not trained yet')

    y = current_model.predict(np.array([x]))
    return y[0][0]