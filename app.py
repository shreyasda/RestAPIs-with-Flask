from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name" : "My Store",
        "items" : [
            {
                "name" : "Pen",
                "price" : 10
            }
        ]
    }
]

#Send a GET request
@app.get("/store") #http://127.0.0.1:5000/store
def get_stores():
    return {"stores": stores}

#Send a POST request
@app.post("/store")
def create_store(): #http://127.0.0.1:5000/store
    request_data = request.get_json() #Fetch data from API Client
    new_store = {"name": request_data["name"], "items": []} #Create a Dictionary
    stores.append(new_store)
    return new_store, 201 #201 is the status code

#Send a custom POST request
@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json() #Fetch data from API Client
    for store in stores:
        if store["name"] == name: #Check whether store already exists
            new_item = {"name":request_data["name"], "price":request_data["price"]} # Add new item to the store
            store["items"].append(new_item) 
            return new_item, 201
    return {"message":"Store not found"}, 404 #Display this if the store is not found

#Send a GET request to get the Individual Store details
@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message":"Store not found"}, 404 #Display this if the store is not found

#Send a GET request to get the details of an Item in the store
@app.get("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return {"items":store["items"]}
    return {"message":"Store not found"}, 404 