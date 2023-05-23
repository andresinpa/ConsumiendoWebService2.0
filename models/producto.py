from utils.db import db

class Producto(db.Model):
    #__tablename__ = 'producto'
    id = db.Column(db.Integer, primary_key=True)
    nombreProducto = db.Column(db.String(100))
    precio = db.Column(db.String(8))
    marca = db.Column(db.String(40))
    descripcion = db.Column(db.String(300))
    
    def __init__(self, nombreProducto, precio, marca, descripcion):
        self.nombreProducto = nombreProducto
        self.precio = precio
        self.marca = marca
        self.descripcion = descripcion