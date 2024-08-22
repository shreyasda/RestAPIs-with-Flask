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
def get_store():
    return {"stores": stores}

#Send a POST request
@app.post("/store")
def create_store(): #http://127.0.0.1:5000/store
    request_data = request.get_json() #Fetch data from API Client
    new_store = {"name": request_data["name"], "items": []} #Create a Dictionary
    stores.append(new_store)
    return new_store, 201 #201 is the status code
