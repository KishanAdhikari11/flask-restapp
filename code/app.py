from flask import Flask
from flask_jwt import JWT
from flask_restful import Api
from security import authenticate,identity
from user import UserRegister
from item import Item,ItemList


app=Flask(__name__)
api=Api(app)

jwt=JWT(app,authenticate,identity)

api.add_resource(Item,'/items/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register')




if __name__=='__main__':
    app.run(port=4000,debug=True)

