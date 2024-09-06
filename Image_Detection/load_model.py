import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler

# Model loading and health forecasting functions
def load_pretrained_model(model_path='model/lstm_model.h5'):
    """Load the pre-trained LSTM model."""
    return tf.keras.models.load_model(model_path)

def prepare_data(data, scaler, time_steps=10):
    """Prepare data for LSTM model."""
    scaled_data = scaler.transform(data)
    X = [scaled_data[i:(i + time_steps), :] for i in range(len(data) - time_steps)]
    return np.array(X)

def forecast_plant_health(sensor_data, model, scaler):
    """Forecast plant health based on the input sensor data."""
    scaled_data = scaler.transform(sensor_data)
    scaled_data = np.expand_dims(scaled_data, axis=0)
    prediction = model.predict(scaled_data)
    return 'Healthy' if prediction[0][0] > 0.5 else 'Diseased'
