import sqlite3

class User:
    def __init__(self,_id,username,password):
        self.id=_id
        self.username=username
        self.password=password
    def find_by_username(self,username):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()

        query="SELECT * FROM users WHERE username=?"
        result=cursor.execute(query,(username,))
        row=result.fetchone()
        if row:
            user=User(*row)
        else:
            user=None
        connection.close()
        return user

    @classmethod
    def find_by_id(cls,id):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()

        query="SELECT * FROM users WHERE id=?"
        result=cursor.execute(query,(id,))
        row=result.fetchone()
        if row:
            user=User(*row)
        else:
            user=None
        connection.close()
        return user