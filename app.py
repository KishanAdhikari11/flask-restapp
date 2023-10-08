from flask import Flask,jsonify,request
from flask_restful import Resource,Api



app=Flask(__name__)

stores=[
    {
        'name':'My wonderful store',
        'items': [
            {
                'name': 'My Item',
                'Price': 15.99
            }
        ]
    }
]
@app.route('/')
def home():
    return '<p> Hello, World </p>'

@app.route('/store ',methods=['POST'])
def create_store():
    request_data=request.get_json()
    new_store={
        'name':request_data['name'],
        'items' : []
    }
    stores.append(new_store)
    return jsonify(new_store)
 
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name']==name:
            return jsonify(store)
        else:
            return jsonify({"message":"Not Found"})



@app.route('/stores/')
def  get_stores():
    return jsonify({'stores':stores})

@app.route('/store/<string:name>/item',method=['POST'])
def create_item_in_store(name):
    request_data=request.get_json()
    for store in stores:
        if store['name']==name:
            new_item={
                'name':request_data['name'],
                'price': request_data['price']

            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found'})

                   
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['items']==name:
            return jsonify(store['items'])
        else:
            return jsonify({'message':'item not found'})




app.run(port=4000)