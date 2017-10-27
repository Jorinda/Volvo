from CarController import CarList, Car, addInfoFromRequest
from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/cars', methods=['GET', 'POST'])
def cars_page():
    
    if request.method == 'POST':
        name = request.form['submit']
        made_in = Car(name).made_in
        height = Car(name).height
        length = Car(name).length
        productionStart = Car(name).productionStart
        productionEnd = Car(name).productionEnd
        successor = Car(name).successor
        predecessor = Car(name).predecessor
        description = Car(name).description
        if made_in == "(unknown information)" or height == "(unknown information)" or length == "(unknown information)" or description == "(unknown information)" or productionEnd == "(unknown information)" or productionStart == "(unknown information)" or successor == "(unknown information)" or predecessor == "(unknown information)":
            return render_template('car_empty.html', car = name, made_in = made_in, height = height, length = length, productionStart = productionStart, productionEnd = productionEnd, successor = successor, predecessor = predecessor, description = description)
        else:
            return render_template('car.html', car = name, made_in = made_in, height = height, length = length, productionStart = productionStart, productionEnd = productionEnd, successor = successor, predecessor = predecessor, description = description)
    if request.method == 'GET': 
        li = CarList().li
        return render_template('cars.html', cars = li)

@app.route('/add_info', methods=['GET', 'POST'])
def add_info():
           
    if request.method == 'PUT':
        li = CarList().li
        return render_template('cars.html', cars = li)

@app.route('/add_info/<car>', methods=['GET','POST'])
def show(car):
    if request.method == 'GET':
        return render_template('addInfo.html', car = car)
    if request.method == 'POST':     
        g = addInfoFromRequest(request)
        print g.serialize(format='turtle')
        li = CarList().li
        return render_template('cars.html', cars = li)

if __name__ == '__main__':
    app.run(debug=True)
    
    


