from peewee import *

# Create an instance of database and make the connection with SQLite db
db = SqliteDatabase('sensors.db', check_same_thread=False)

# Create data model class that inherit from Peewee ORM Model class
class Sensor(Model):
    
    name = CharField()
    sensor_type = IntegerField()
    pin = IntegerField()
    
    class Meta:
        database = db 


class Sensor_Reading(Model):
    
    time = DateTimeField()
    name = CharField()
    value = FloatField()

    class Meta:
        database = db

# Provides functions to query the sensor
# Connect to database and create the tables in database
# Define sensor and add to db
# Return a list of all sensors in db
# Add the sensor's reading to db
# Close the db connection
class SensorData(object):

    def __init__(self):
        db.connect()
        db.create_tables([Sensor, Sensor_Reading], safe=True)

    def define_sensor(self, name, sensor_type, pin):
        Sensor.get_or_create(name=name, sensor_type=sensor_type, pin=pin)

    def get_sensors(self):
        return Sensor.select()

    def add_reading(self, time, name, value):
        Sensor_Reading.create(time=time, name=name, value=value)

    def close(self):
        db.close()
