from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from models.producto import Producto
from utils.db import db, ma

class ProductosSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombreProducto', 'precio', 'marca', 'descripcion')

productos = Blueprint('productos', __name__)
producto_schema = ProductosSchema()
productos_schema = ProductosSchema(many=True)

#Para consumir web service INICIO----------------------
#GET
@productos.route('/productos/<id>', methods=(['GET']))
def getProducto(id):
    producto = Producto.query.get(id)
    return producto_schema.jsonify(producto)

@productos.route('/productos', methods=['GET'])
def getProductos():
    all_productos = Producto.query.all()
    results = productos_schema.dump(all_productos)
    return jsonify(results)

#POST
@productos.route('/productos', methods=['POST'])
def create_producto():
    nombreProducto = request.json['nombreProducto']
    precio = request.json['precio']
    marca = request.json['marca']
    descripcion = request.json['descripcion']
    
    new_producto = Producto(nombreProducto, precio, marca, descripcion)
    db.session.add(new_producto)
    db.session.commit()
    
    return producto_schema.jsonify(new_producto)

#PUT
@productos.route('/productos/<id>', methods=(['PUT']))
def updateProducto(id):
    producto = Producto.query.get(id)
    nombreProducto = request.json['nombreProducto']
    precio = request.json['precio']
    marca = request.json['marca']
    descripcion = request.json['descripcion']
    
    producto.nombreProducto = nombreProducto
    producto.precio = precio
    producto.marca = marca
    producto.descripcion = descripcion

    db.session.commit()
    return producto_schema.jsonify(producto)

#DELETE
@productos.route('/productos/<id>', methods=(['DELETE']))
def deleteProducto(id):
    producto = Producto.query.get(id)
    db.session.delete(producto)
    db.session.commit()
    return producto_schema.jsonify(producto)

#Para consumir web service FIN-----------------------


@productos.route('/')
def index():
    productos = Producto.query.all()
    return render_template('index.html', productos=productos)

@productos.route('/new', methods=['POST'])
def add_producto():
    nombreProducto = request.form['nombreProducto']
    precio = request.form['precio']
    marca = request.form['marca']
    descripcion = request.form['descripcion']
    new_producto = Producto(nombreProducto, precio, marca, descripcion)
    #print(new_producto)
    db.session.add(new_producto)
    db.session.commit()
    
    flash("¡Producto agregado satisfactoriamente!")
    
    return redirect(url_for('productos.index'))

@productos.route('/update/<id>', methods=['POST', 'GET'])
def update_producto(id):
    producto = Producto.query.get(id)
    if request.method == 'POST':
        producto.nombreProducto = request.form['nombreProducto']
        producto.precio = request.form['precio']
        producto.marca = request.form['marca']
        producto.descripcion = request.form['descripcion']
        
        db.session.commit()
        flash("¡Producto actualizado satisfactoriamente!")
        return redirect(url_for("productos.index"))
        
    return render_template('update.html', producto=producto)


@productos.route('/delete/<id>')
def delete_producto(id):
    producto = Producto.query.get(id)
    #print(producto)
    db.session.delete(producto)
    db.session.commit()
    flash("¡Producto eliminado satisfactoriamente!")
    return redirect(url_for('productos.index'))

@productos.route('/about')
def acerca():
    return render_template('about.html')
