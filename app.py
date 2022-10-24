from flask import Flask, request

app = Flask(__name__)

stores = [ # Stores is a list of dictionaries. Each store has a list of dictionaries of items. 
{
    "name": "My Store",
    "items": [ # list of dictionaries. Can have multiple items, where each item is a dictionary. 
        {
            "name":"Chair",
            "price":15.99
        }
    ]
}
]

@app.get("/store") #this is the endpoint. http://127.0.0.1:5000/store
def get_stores(): #function associated with this endpoint
    return {"stores":stores}

@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name":request_data["name"],"items":[]}
    stores.append(new_store)
    return new_store, 201 #201 tells the system that not only is everything okay, but a new store was created. #more specifically that a new resource was created.

@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name":request_data["name"],"price":request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message":"Store not found"}, 404

@app.get("/store/<string:name>") 
def get_store(name): #function associated with this endpoint
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "Store not found"}, 404

@app.get("/store/<string:name>/item") 
def get_item_in_store(name): #function associated with this endpoint
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message": "Store not found"}, 404