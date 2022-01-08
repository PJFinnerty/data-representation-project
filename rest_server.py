
from flask import Flask, url_for, request, redirect, abort, jsonify

app = Flask(__name__, static_url_path='', static_folder='static_pages')

books = [
    {"id":1, "Title":"Harry Potter", "Author":"JK Rowling", "Prics":10},
    {"id":2, "Title":"Moby Dick", "Author":"Herman Melville", "Prics":4},
    {"id":3, "Title":"THeir Eyes were Watching God", "Author":"Zora Neale Hurston", "Prics":9}    
]

nextId = 4

@app.route('/')
def index():
    return "hello"
    #return redirect (url_for('login'))
    
@app.route('/books')
def getAll():
    return jsonify(books)
   
# Find By ID   
@app.route('/books/<int:id>')
def findById(id):
    foundBooks = list(filter (lambda t : t["id"]== id, books))
    print(foundBooks)
    if len(foundBooks) == 0:
        return jsonify({}), 204
    return jsonify(foundBooks[0])
    #return "served by findById with id "+str(id)

# Create 
# code for create command: curl -X POST -H "content-type:application/json" -d "{\"Title\":\"test\", \"Author\":\"Some Guy\",\"Price\":123}" http://127.0.0.1:5000/books   
@app.route('/books', methods=['POST'])
def create():
    global nextId
    if not request.json:
        abort(400)
    book = {
        "id":nextId, 
        "Title":request.json["Title"],
        "Author": request.json["Author"], 
        "Price": request.json["Price"]
    }
    books.append(book)
    nextId += 1
    return jsonify(book)

#Update
# Sample curl command for Update function: curl -X PUT -H "content-type:application/json" -d "{\"New\":\"test\",\"Price\":999}" http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>', methods=['PUT'])
def showUpdate(id):
    foundBooks = list(filter (lambda t : t["id"]== id, books))
    print(foundBooks)
    if len(foundBooks) == 0:
        return jsonify({}), 404
    currentBook = foundBooks[0]
    if 'Title' in request.json:
        currentBook['Title'] = request.json['Title']
    if 'Author' in request.json:
        currentBook['Author'] = request.json['Author']
    if 'Price' in request.json:
        currentBook['Price'] = request.json['Price']        
    return jsonify(currentBook)
  
# Delete  
@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    foundBooks = list(filter (lambda t : t["id"]== id, books))
    print(foundBooks)
    if len(foundBooks) == 0:
        return jsonify({}), 404
    books.remove(foundBooks[0])

    return jsonify({"done":True})

if __name__ == "__main__" :
    print("in if")
    app.run(debug=True)
    
# Need to do Client Side Challenge Lab of Cient Side interacting with Server
    
    