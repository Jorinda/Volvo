import os
from rdflib import Graph, RDF, Namespace, Literal, URIRef, RDFS
g = Graph()

class CarList:
    #this function will get all the car names in the instances.ttl file to the html page
    def __init__(self):
        self.li = []
        fileDir = os.path.dirname(os.path.realpath('resources\instances.ttl'))
        filename = os.path.join(fileDir, 'instances.ttl')
        with open(filename) as file:
            content = file.readlines()
        for l in content:
            if l.startswith('dbr'):
                car = l.split('"')
                self.li.append(car[1])

class Car():
    #this function will pass information about the clicked carname to the html
    def __init__(self, name):
        self.made_in = "(unknown information)"
        self.height = "(unknown information)"
        self.length = "(unknown information)"
        self.productionStart = "(unknown information)"
        self.productionEnd = "(unknown information)"
        self.successor = "(unknown information)"
        self.predecessor = "(unknown information)"
        self.description = "(unknown information)"
        g = Graph()
        def serialize():
            print g.serialize(format='turtle')

        def save(filename):
            with open(filename, 'w') as f:
                g.serialize(f, format='turtle')
        
        def load(filename):
            with open(filename, 'r') as f:
                g.load(f, format='turtle')   
        load('resources\properties.ttl')
        subject = name.replace(' ', '_')
        factories = []
        for s,p,o in g:
            s = s.split("/")
            s = s[-1]
            p = p.split("#")
            p = p[-1]
            o = o.split("/")
            o = o[-1]
            if s == subject and p == "made_in":                
                factories.append(o)
                self.made_in = factories[0]            
            elif s == subject and p == "height":
                self.height = o
            elif s == subject and p == "productionStart":  
                self.productionStart = o
            elif s == subject and p == "productionEnd": 
                self.productionEnd = o
            elif s == subject and p == "successor":
                self.successor = o
            elif s == subject and p == "predecessor":
                self.predecessor = o
            elif s == subject and p == "description":
                self.description = o
            elif s == subject and p == "length":
                self.length = o   

def addInfo(name, made_in, height, length, productionStart,  productionEnd, successor, predecessor, description):
    
    def serialize():
        print g.serialize(format='turtle')
    def save(filename):
        with open(filename, 'w') as f:
            g.serialize(f, format='turtle')
    def load(filename):
        with open(filename, 'r') as f:
            g.load(f, format='turtle')   
    load('resources\properties.ttl')
    name = name.replace(" ", "_")
    EX = Namespace(u'http://example.com/kad2017/')
    g.bind('new',EX)
    s = EX[name]
    p = EX["new#"]
    g.add((s, Literal(p + "made_in"), Literal(made_in)))
    g.add((s, Literal(p + "height"), Literal(height)))
    g.add((s, Literal(p +"length"), Literal(length)))
    g.add((s, Literal(p + "productionStart"), Literal(productionStart)))
    g.add((s, Literal(p + "productionEnd"), Literal(productionEnd)))
    g.add((s, Literal(p + "description"), Literal(description)))
    g.add((s, Literal(p + "successor"), Literal(successor)))
    g.add((s, Literal(p + "predecessor"), Literal(predecessor)))
    
    save('resources\properties.ttl')
    return g

def save(filename):
    with open(filename, 'w') as f:
        g.serialize(f, format='turtle')

def addInfoFromRequest (request):
        name = request.form['name']
        made_in = request.form['made_in']
        height = request.form['height']
        length = request.form['length']
        productionStart = request.form['productionStart']
        productionEnd = request.form['productionEnd']
        successor = request.form['successor']
        predecessor = request.form['predecessor']
        description = request.form['description'] 
        return addInfo(name, made_in, height, length, productionStart,  productionEnd, successor, predecessor, description)