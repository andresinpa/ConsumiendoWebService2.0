from flask import Blueprint, flash, redirect, render_template, request, url_for
from models.producto import Producto
from utils.db import db

productos = Blueprint('productos', __name__)
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
