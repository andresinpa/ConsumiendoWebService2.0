from flask import Flask
from routes.productos import productos
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = "secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://u3cxcelzhxt9xtos:DiEB2jQOnqztF6ubC6Gk@bupauath6phqcmgrvfr8-mysql.services.clever-cloud.com/bupauath6phqcmgrvfr8'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/productosbd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


app.register_blueprint(productos)
 


