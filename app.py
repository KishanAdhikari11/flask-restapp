from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from security import authenticate,identity
from resources.user import UserRegister
from resources.item import Item,ItemList


app=Flask(__name__)
app.secret_key='jose'
api=Api(app)

jwt=JWTManager(app)

api.add_resource(Item,'/items/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register')




if __name__=='__main__':
    app.run(port=4000,debug=True)

