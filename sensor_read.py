#!/usr/bin/python
import sys
import sqlite3
import Adafruit_DHT
import time
humidity, temperature = Adafruit_DHT.read_retry(11, 4)

#  Open SQLite database connection
conn = sqlite3.connect('sensors.db')

# Create cursor object
c = conn.cursor()

# Execute() method is called to perform SQL commands
c.execute('SELECT name, type, pin FROM sensors')

# List of sensors set to be empty
sensors = []

# Read all the rows and print
for row in c:
    name, sensor_type, pin = row
    print('Sensor: {0}   Type: {1}   Pin: {2}'.format(name, sensor_type, pin))

    # Convert the string to actual library value
    if sensor_type == 'Temperature':
        sensor_type = Adafruit_DHT.DHT11
        
    else:
        raise RuntimeError('Unknown sensor: {0}'.format(sensor_type))

    # Append the details of the sensor
    sensors.append((name, sensor_type, pin))

    #print(sensors)

# Loop through all the sensors
while True:
    for s in sensors:
        readTime = int(time.time())
        name, sensor_type, pin = s
        humidity, temperature = Adafruit_DHT.read_retry(11, 4)
        print('Sensor: {0}, Humidity = {1:0.2f}%, Temperature = {2:0.2f}C'.format(name, humidity, temperature))

        # Insert the sensor readings into the readings table
        c.execute('INSERT INTO sens_readings VALUES (?, ?, ?)',
                  (readTime, '{0} Humidity'.format(name), humidity))
        c.execute('INSERT INTO sens_readings VALUES (?, ?, ?)',
                  (readTime, '{0} Temperature'.format(name), temperature))

        # Commit the changes
        conn.commit()
                  
    time.sleep(3)
    
