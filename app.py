from flask import Flask
from routes.productos import productos
from flask_sqlalchemy import SQLAlchemy
from utils.db import db

app = Flask(__name__)

app.secret_key = "secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://u3cxcelzhxt9xtos:DiEB2jQOnqztF6ubC6Gk@bupauath6phqcmgrvfr8-mysql.services.clever-cloud.com:3306/bupauath6phqcmgrvfr8'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://JesusInfante:productos1234@JesusInfante.mysql.pythonanywhere-services.com/JesusInfante$productosbd'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/productosbd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(productos)
 
with app.app_context():
    db.init_app(app)
    db.create_all()
 
if __name__ == "__main__":
    
    app.run(debug=True)


