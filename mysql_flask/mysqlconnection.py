"""import the necessary modules"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

class MYSQLConnection(object):
    def __init__(self, app, db):

        config = {
            'host': 'localhost',
            'database': db,
            'user': 'root',
            'password': 'reddragon',
            'port': '3306',
        }

        # this will use the above values  to generate the path to connect to your sql database
        DATABASE_URI = "mysql://{}:{}@127.0.0.1:{}/{}".format(config['user'], config['password'], config['port'],
                                                             config['database'])
        app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        # establish the connection to database
        self.db = SQLAlchemy(app)

    def exec_db(self,command,data=None):
        result =  self.db.session.execute(text(command), data)
        return result

def MYSQLConnector(app, db):
    return MYSQLConnection(app, db)