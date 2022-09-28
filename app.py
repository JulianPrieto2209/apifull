from xmlrpc.client import Marshaller
from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os




#Mensaje de bienvenida
@app.route('/a')
def index():
    return "<h1>Hola<h1>"

if __name__ == '__main__':
    app.run(port = int(os.environ.get('PORT', 5000)))