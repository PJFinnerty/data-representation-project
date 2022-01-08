from flask import Flask, jsonify, request, abort
from deliveryDAO import deliveryDAO

app = Flask(__name__, static_url_path='', static_folder='.')

#curl "http://127.0.0.1:5000/delivery"
@app.route('/delivery')
def findAll():
    #print("in findAll")
    results = deliveryDAO.findAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/delivery/2"
@app.route('/delivery/<int:id>')
def findItem(id):
    foundBook = deliveryDAO.findItem(id)

    return jsonify(foundBook)

if __name__ == '__main__' :
    app.run(debug= True)
    
    
    