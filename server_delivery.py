from flask import Flask, jsonify, request, abort
from deliveryDAO import deliveryDAO

app = Flask(__name__, static_url_path='', static_folder='.')

@app.route('/delivery')
def findAll():
    #print("in findAll")
    results = deliveryDAO.findAll()
    return jsonify(results)

@app.route('/delivery/<int:id>')
def findItem(id):
    foundItem = deliveryDAO.findItem(id)
    return jsonify(foundItem)

@app.route('/delivery', methods=['POST'])
def create():  
    if not request.json:
        abort(400)
    delivery = {
        "Item": request.json['Item'],
        "Type": request.json['Type'],
        "Quantity": request.json['Quantity'],
        "TotPrice": request.json['TotPrice'],
    }
    values =(delivery['Item'],delivery['Type'],delivery['Quantity'], delivery['TotPrice'])
    newId = deliveryDAO.create(values)
    delivery['id'] = newId
    return jsonify(delivery)

@app.route('/delivery/<int:id>', methods=['PUT'])
def update(id):
    foundItem = deliveryDAO.findItem(id)
    if not foundItem:
        abort(404)   
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'TotPrice' in reqJson and type(reqJson['TotPrice']) is not int:
        abort(400)
    if 'Quantity' in reqJson and type(reqJson['Quantity']) is not int:
        abort(400)
    if 'Item' in reqJson:
        foundItem['Item'] = reqJson['Item']
    if 'Type' in reqJson:
        foundItem['Type'] = reqJson['Type']
    if 'Quantity' in reqJson:
        foundItem['Quantity'] = reqJson['Quantity']
    if 'TotPrice' in reqJson:
        foundItem['TotPrice'] = reqJson['TotPrice']
    values = (foundItem['Item'],foundItem['Type'],foundItem['Quantity'],foundItem['TotPrice'],foundItem['id'])
    deliveryDAO.update(values)
    return jsonify(foundItem)
        
@app.route('/delivery/<int:id>' , methods=['DELETE'])
def delete(id):
    deliveryDAO.delete(id)
    return jsonify({"done":True})


if __name__ == '__main__' :
    app.run(debug= True)
    
      