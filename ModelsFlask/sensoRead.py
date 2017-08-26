import Adafruit_DHT
from model import SensorData
import time
from datetime import datetime

data = SensorData()

data.define_sensor('DHT', Adafruit_DHT.DHT11, 4)

try:
    while True:
        readingTime = datetime.now()
        
        for sensor in data.get_sensors():       
            humidity, temperature = Adafruit_DHT.read_retry(sensor.sensor_type, sensor.pin)
            print('Sensor: {0}, Humidity = {1:0.2f}%, Temperature = {2:0.2f}C'.format(sensor.name, humidity, temperature))
            data.add_reading(readingTime, '{0} Humidity,'.format(sensor.name), humidity)
            data.add_reading(readingTime, '{0} Temperature,'.format(sensor.name), temperature)
    time.sleep(1.0)
finally:
    data.close()
