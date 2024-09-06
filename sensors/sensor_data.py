import random

# Functions for testing sensor data
def get_temperature():
    """Simulate getting temperature data from the sensor."""
    return round(random.uniform(20.0, 35.0), 2)

def get_humidity():
    """Simulate getting humidity data from the sensor."""
    return round(random.uniform(30.0, 90.0), 2)

def get_soil_moisture():
    """Simulate getting soil moisture data from the sensor."""
    return round(random.uniform(0.1, 1.0), 2)

def read_sensor_data():
    """Collect sensor data for processing."""
    temp = get_temperature()
    humidity = get_humidity()
    moisture = get_soil_moisture()
    return [[temp, humidity, moisture]]
