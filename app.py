from flask import Flask
from flask_restful import Resource,Api

app=Flask(__name__)
api=Api(app)
items=[]
class Item(Resource):
    def get(self,name):
        for item in items:
            if item['name']==name:
                return item
        return {'item':"Not found"},404
    
    def post(self,name):
        item={"price":25.00,'name':name}
        items.append(item)
        return item,201
api.add_resource(Item,'/item/<string:name>')
app.run(port=5000)
