import sqlite3
from flask import jsonify
from flask_restful import Resource,Api,reqparse
from flask_jwt_extended import jwt_required
from models.item import ItemModel


class Item(Resource): 
     parser=reqparse.RequestParser()
     parser.add_argument('price',
                        type=float,
                        required=True,
                        help='This field cannot be left blank!'
                            )
     

     @jwt_required()
     def get(self,name):
       item=ItemModel.find_by_name(name)
       if item:
           return item
       return {'message':'Item not found'},404
     
     
     @jwt_required()
     def post(self,name):
         if Item.find_by_name(name):
             return {'message':"An item with name '{}' already exists.".format(name)},400
         data=Item.parser.parse_args()
         item=ItemModel(name,data['price'])
         
         try:
             item.insert()
         except:
             return {'message':"An error occured inserting the item"},500
         return item.json()
            
         return item,201
     @jwt_required()
     def delete(self,name):
         connection=sqlite3.connect('data.db')
         cursor=connection.cursor()
         query="DELETE FROM items WHERE name=?"
         cursor.execute(query,(name,))
         connection.commit()
         connection.close()
         return {'message':"Item deleted"}
         
     @jwt_required()
     def put(self,name):
        data=Item.parser.parse_args()
        item=ItemModel.find_by_name(name)
        updated_item=ItemModel(name,data['price'])
        if item is None:
            try:
              updated_item.insert()
                
            except:
                return {"message":"An error occured inserting the item"},500
        else: 
            try:
                updated_item.update()
            except:
                return {"message":"An error occured updating the item"},500
        return updated_item
     
     
class ItemList(Resource):
    def get(self):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        query='SELECT * FROM items'
        result=cursor.execute(query)
        item=[]
        for row in result:
            item.append({'name':row[0],'price':row[1]})
    
        connection.close()
        return {'items':item}
         


