from models.user import UserModel
from flask_jwt_extended import create_access_token
def authenticate(username,password):
    user=UserModel.find_by_username(username)
    if user and user.password==password:
        access_token=create_access_token(identity=user.id)
        return access_token

def identity(payload):
    user_id=payload['identity']
    return UserModel.find_by_id(user_id,None)

