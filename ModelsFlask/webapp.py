from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.peewee import ModelView

import model

app = Flask(__name__)
app.config['SECRET_KEY'] = '1908'
# Database model access class
app.config['MODEL'] = model.SensorData()

admin = Admin(app, name='SQLite Sensors', template_mode='bootstrap3')
admin.add_view(ModelView(model.Sensor))
admin.add_view(ModelView(model.Sensor_Reading))

