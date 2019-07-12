from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Home/andre/Desktop/Voice-recognition'
db = SQLAlchemy(app)
#Script to create DB to receive voiceapp and time.
conn = sqlite3.connect('voiceapp.db')
print ("Opened database successfully")

conn.execute('CREATE TABLE voice (id INTEGER PRIMARY KEY AUTOINCREMENT,temperature VARCHAR, time DATETIME)')
print ("Table created successfully")
conn.close()

class voiceapp(db.voiceapp):
    id = db.Column ( 'id', db.Integer,primary_key=True)
    temperaure = db.Column('temperature', db.VARCHAR(80), unique=True, nullable=False)
    time = db.Column('time', db.DATETIME, unique=True, nullable=False)

    def __repr__(self):
        return f"data('{self.id}','{self.temperature}','{self.time}')"