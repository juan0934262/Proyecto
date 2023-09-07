from flask import Flask, render_template, request, Response, jsonify, redirect, url_for

import Modelos as dbase
from Product import Product

db = dbase.dbConnection()
app=Flask(__name__)

@app.route('/')
def Inicio():
    return render_template('/index.html')

@app.route('/proyect', methods=['POST'])
def addInicio():
    products = db['products']
    Nombre = request.form['Nombre']
    Contraseña = request.form['Contraseña']

    if Nombre and Contraseña:
      product = Product(Nombre, Contraseña)
      products.insert_one(product.toDBCollection())
      response = jsonify({
       'Nombre' : Nombre,
       'Contraseña' : Contraseña,
      })
      return redirect(url_for('Inicio'))
    else:
        return notFound()

#Método de error
@app.errorhandler(404)
def notFound(error=None):
  message ={
    'message': 'No encontrado ' + request.url,
    'status': '404 Not Found'
  }
  response = jsonify(message)
  response.status_code = 404
  return response